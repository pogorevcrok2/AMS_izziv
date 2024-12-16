## AMS izziv 
<!-- -->

## Disclaimer 
This is a student project
<!-- 
# docker build . -t deepreg -f Dockerfile
# docker run --name DeepReg --privileged=true --gpus all -ti deepreg bash


# cd C:\Users\Pogorevc\OneDrive - Univerza v Ljubljani\Magisterij\2. Letnik\AMS_izziv\DeepReg
# cd C:\Users\Pogorevc\OneDrive - Univerza v Ljubljani\Magisterij\2. Letnik\AMS_izziv\Validation\deformable-registration\deformable-registration

# docker build . -t evaluation -f Dockerfile

docker run --rm -it -v "C:\Users\Pogorevc\OneDrive - Univerza v Ljubljani\Magisterij\2. Letnik\AMS_izziv\Validation\deformable-registration\deformable-registration\input:/input" -v "C:\Users\Pogorevc\OneDrive - Univerza v Ljubljani\Magisterij\2. Letnik\AMS_izziv\Validation\deformable-registration\deformable-registration\output:/output/" -v ./data:/workspace/data evaluation python evaluation.py -v



# docker start -i DeepReg1


# pip install pydot
# apt-get update && apt-get install -y graphviz
# pip uninstall tensorflow-gpu tensorflow
# pip install tensorflow-gpu==2.10.0
# python AMS/ams_data.py

#python AMS/ams_data.py
#python AMS/ams_data2.py
#python AMS/ams_train.py --full
#python AMS/ams_predict.py --full

#deepreg_vis -m 2 -i 'AMS/ams/logs_predict/20241216-190428/test/pair_0/moving_image.nii.gz, AMS/ams/logs_predict/20241216-190428/test/pair_0/pred_fixed_image.nii.gz, AMS/ams/logs_predict/20241216-190428/test/pair_0/fixed_image.nii.gz' --slice-inds '64,50,72' -s AMS/ams/logs_predict/

#deepreg_vis -m 1 -i 'AMS/ams/logs_predict/20241216-190428/test/pair_0/moving_image.nii.gz --ddf-path "AMS/ams/logs_predict/20241216-190428/test/pair_0/ddf.nii.gz" --slice-inds '2,3' -s AMS/ams/logs_predict/


-->



# AMS IZZIV - final report
ROK POGOREVC

<p align="center">
  <img src="https://raw.githubusercontent.com/DeepRegNet/DeepReg/main/docs/asset/deepreg_logo_purple.svg"
    alt="deepreg_logo" title="DeepReg" width="200"/>
</p>

# DeepReg
Original code and documentation available at: https://github.com/DeepRegNet/DeepReg

## Method Explanation
Describe the method used in your project in your own words. Explain the key concepts and steps involved. If applicable, include figures. 

## Results
Include some of *your* results here. Make sure to include aggregated results and any relevant images.

```bash
 aggregated results:
	LogJacDetStd        : 0.10320 +- 0.00834 | 30%: 0.10965
	TRE_kp              : 7.69219 +- 2.03832 | 30%: 7.36717
	TRE_lm              : 8.51688 +- 3.86951 | 30%: 8.24852
	DSC                 : 0.55044 +- 0.13053 | 30%: 0.49095
	HD95                : 33.87484 +- 10.90554 | 30%: 23.67392
```


## Docker Information
Provide information on how to set up and use Docker for this project. Be very specific when writing about Docker installation. Include step-by-step instructions, commands, and any necessary configurations. 

## Data Preparation
Explain the steps required to prepare the data for training. Include any preprocessing steps and data splitting.

## Train Commands
If applicable, list the commands needed to train your model. Provide any necessary explanations or parameters. 
For train.py script, you should use a parser to set all input parameters. Below is the example, how to run `train.py`:

```bash
python train.py --i /path/to/data --o /path/to/models -other /other/parameters....
```

Make sure to include ` path to data`, `path where to save models` and all user related parameters in parser.

## Test Commands
List the commands needed to test your model. Provide any necessary explanations or parameters.
For test.py script, you should use a parser to set all input parameters. Below is the example, how to run `test.py`:

```bash
python test.py --i /path/to/test/data --o /path/to/output -other /other/parameters....
```

Make sure to include `path to test data`, `path where to save output` and all user related parameters in parser.


---

### Results from provided code
```bash
case_results [0] [0011_0001<--0011_0000']:
        LogJacDetStd        : 0.02350
        num_foldings        : 0.00000
        TRE_kp              : 16.95331
        TRE_lm              : 19.65747
        DSC                 : 0.15308
        HD95                : 36.51497
case_results [1] [0012_0001<--0012_0000']:
        LogJacDetStd        : 0.02554
        num_foldings        : 0.00000
        TRE_kp              : 13.85208
        TRE_lm              : 14.40804
        DSC                 : 0.28575
        HD95                : 35.12166
case_results [2] [0013_0001<--0013_0000']:
        LogJacDetStd        : 0.02317
        num_foldings        : 0.00000
        TRE_kp              : 21.06048
        TRE_lm              : 23.39744
        DSC                 : 0.10483
        HD95                : 70.89763
case_results [3] [0011_0002<--0011_0000']:
        LogJacDetStd        : 0.02354
        num_foldings        : 0.00000
        TRE_kp              : 16.61175
        TRE_lm              : 14.99693
        DSC                 : 0.15450
        HD95                : 54.61209
case_results [4] [0012_0002<--0012_0000']:
        LogJacDetStd        : 0.02538
        num_foldings        : 0.00000
        TRE_kp              : 22.65494
        TRE_lm              : 25.91111
        DSC                 : 0.10708
        HD95                : 40.49948
case_results [5] [0013_0002<--0013_0000']:
        LogJacDetStd        : 0.02302
        num_foldings        : 0.00000
        TRE_kp              : 15.45530
        TRE_lm              : 17.91634
        DSC                 : 0.20790
        HD95                : 67.24160

 aggregated_results:
        LogJacDetStd        : 0.02403 +- 0.00103 | 30%: 0.02446
        TRE_kp              : 17.76464 +- 3.09317 | 30%: 19.00689
        TRE_lm              : 19.38122 +- 4.18223 | 30%: 21.52746
        DSC                 : 0.16886 +- 0.06266 | 30%: 0.13008
        HD95                : 50.81457 +- 14.40339 | 30%: 38.50722

```
