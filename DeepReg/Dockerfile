FROM tensorflow/tensorflow:2.10.0-gpu

# install miniconda
ENV CONDA_DIR=/root/miniconda3
ENV PATH=${CONDA_DIR}/bin:${PATH}
ARG PATH=${CONDA_DIR}/bin:${PATH}
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-get update
RUN apt-get install -y wget git && rm -rf /var/lib/apt/lists/*

#ENV LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64:$LD_LIBRARY_PATH
#ENV TF_FORCE_GPU_ALLOW_GROWTH=true
#ENV NVIDIA_VISIBLE_DEVICES=all

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

# directory for following operations
WORKDIR /app

# clone DeepReg
RUN git clone https://github.com/pogorevcrok2/AMS_izziv.git
WORKDIR /app/AMS_izziv/DeepReg
RUN git pull

# install conda env
RUN conda env create -f environment_cpu.yml \
    && conda init bash \
    && echo "conda activate deepreg" >> /root/.bashrc

# install deepreg
ENV CONDA_PIP="${CONDA_DIR}/envs/deepreg/bin/pip"
RUN ${CONDA_PIP} install -e .
