# pylint: disable=line-too-long
import argparse
from datetime import datetime

from deepreg.predict import predict

name = "ams"

# parser is used to simplify testing, by default it is not used
# please run the script with --full flag to ensure non-testing mode
# for instance:
# python script.py --full
parser = argparse.ArgumentParser()
parser.add_argument(
    "--test",
    help="Execute the script with reduced image size for test purpose.",
    dest="test",
    action="store_true",
)
parser.add_argument(
    "--full",
    help="Execute the script with full configuration.",
    dest="test",
    action="store_false",
)
parser.set_defaults(test=False)
args = parser.parse_args()

print(
    "\n\n\n\n\n"
    "=========================================================\n"
    "The prediction can also be launched using the following command.\n"
    "deepreg_predict --gpu '' "
    f"--config_path AMS/{name}.yaml "
    f"--ckpt_path AMS/{name}/dataset/pretrained/ckpt-8000 "
    f"--log_dir AMS/{name} "
    "--exp_name logs_predict "
    "--save_png --split test\n"
    "=========================================================\n"
    "\n\n\n\n\n"
)

log_dir = f"AMS/{name}"
exp_name = "logs_predict/" + datetime.now().strftime("%Y%m%d-%H%M%S")
#ckpt_path = f"{log_dir}/dataset/pretrained/ckpt-8000"
ckpt_path = f"AMS/model_unet_100_epoh/20241215-223943/save/ckpt-100"

config_path = [f"AMS/{name}.yaml"]
if args.test:
    config_path.append("config/test/ams.yaml")

predict(
    gpu="0,1",
    gpu_allow_growth=True,
    ckpt_path=ckpt_path,
    split="valid",
    batch_size=1,
    log_dir=log_dir,
    exp_name=exp_name,
    config_path=config_path,
)
