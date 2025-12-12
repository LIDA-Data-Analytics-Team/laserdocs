---
layout: default
title: Set Up GPU
parent: RMP
has_children: false
---

# Setting up GPU VM for Deep Learning 

If a research group has requested a VM with GPUs as part of their VRE build, there's a decent chance they'll be wanting to do some deep learning. Here are some instructions on GPU setup to enable various deep learning technologies in LASER.

## Install GPU driver

- You'll need to install an NVIDIA GPU driver to enable CUDA libraries to use the GPU(s). Download the driver from NVIDIA's website, put it in the VRE, then ask IT Server team to install it (needs admin).
- Use [NVIDIA's Driver Download helper](https://www.nvidia.com/download/index.aspx?lang=en-us) to get the right driver, choosing options in the dropdown lists that relate to the GPU in the VM:
    - Choose the latest CUDA Toolkit version.
    - Find the VM's GPU specs by searching on Azure's website. Our typical GPU VM is likely to be NC series, e.g. NC12, details of which are in [Azure's VM documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/nc-series).
- Using the above information, at the time of writing, the driver for an NC12 VM can be downloaded using the following dropdown choices:
    - Product Type: Data Center / Tesla
    - Product Series: K-Series
    - Product: Tesla K80
    - Operating System: Windows 10 64-bit
    - CUDA Toolkit: 11.2 (choose later if available)
    - Language: English
- Hit Search > Download, then import downloaded file into VM and ask Server team to install.
- To check the driver installation worked, log into the VM, open CMD and run:<br>`nvidia-smi`
- It should print a table to stdout showing the driver and CUDA toolkit versions.

### Check GPU utilisation

- After setup, if a user ever questions the GPU performance or utilisation, ask them to run the following command in CMD, run their code using the GPU, stop the CMD command, then show us the output file<br>`nvidia-smi --query-gpu=timestamp,utilization.gpu --format=csv --loop=1 >> N:\gpu_util_test.csv`
- The above line of code will get the GPU utilisation % every 1 second, for each GPU device, and append them into the CSV file. To query with different frequency, update the number of seconds set in the --loop flag. We can look at the GPU utilisation over time.

## Deep learning setup in Python

### Tensorflow

- Find Tensorflow GPU's [tested build configurations](https://www.tensorflow.org/install/source_windows#gpu) on Windows for guidance on what software versions are likely to play nicely. If you're setting up a Linux VM, look for the Linux build configs (NB: the instructions below haven't been tested on Linux).
- I highly recommend installing the latest Tensorflow version and compatible dependency versions.
- The versions shown below reproduce a functional Tensorflow GPU environment in an NC12 VM, at the time of writing.
- Create a new conda environment in the Python repo and add a relatively up to date Python version:<br>`conda create -p P:\V0000\V0000_env_00 python=3.8`
- Activate env: `conda activate P:\V0000\V0000_env_00`
- Install CUDA toolkit: `conda install cudatoolkit=11`
- Install cuDNN (may need to try different channels to get the right version): `conda install -c conda-forge cudnn=8`
- Install Tensorflow, the latest version is best. You will most likely need to pip install to get the latest. You don't need tensorflow-gpu (at least, not via pip).<br>`pip install tensorflow`
- Check Tensorflow GPU is working by logging into the VM, opening Anaconda Prompt and running the following:
    - `conda activate P:\path\to\env`
    - `python`
    - `import tensorflow as tf`
    - `tf.config.list_physical_devices('GPU')`
- Python will print a bunch of lines about opening DLL libraries. At the bottom, you should see a list of GPU devices. If so, hooray your work here is done.
- If you see an empty list `[]` that means tensorflow can't use the GPU and you need to change the installation, most likely the version of cudatoolkit and/or tensorflow.
- That's it. Install any other stuff needed in the env; follow steps in the python repo guidance doc to find any software required in all conda envs. Just make sure no further installations attempt to change the versions of tensorflow, cudatoolkit or cudnn installed.

### Pytorch

- Pytorch website has some [help on pytorch setup](https://pytorch.org/get-started/locally/) and configuration.
- By far the easiest way to install pytorch is using pytorch's own conda channel, getting the latest version and letting them handle the dependencies.
- However, the catch is that the binaries in the pytorch channel are hosted in an S3 bucket and currently this can't be accessed within DAT02. I've asked Tom Dacosta about this, but no progress yet.
- So, I recommend installing using pytorch channel, zipping the env, importing into DAT02, unzipping into Python repo, then finishing any extra conda installs in DAT02.
- Create a new conda environment including a relatively up to date Python version:<br>`conda create -p P:\V0000\V0000_env_00 python=3.8`
- Activate env: `conda activate P:\V0000\V0000_env_00`
- Install pytorch and dependencies from pytorch channel:<br>`conda install -c pytorch pytorch`
- Get the environment into DAT02 as described above.
- Check Pytorch GPU is working by logging into the VM, opening Anaconda Prompt and running the following:
    - `import torch`
    - `torch.cuda.is_available()`
        - If the GPU is working, this will print True.
    - `torch.cuda.device_count()`
        - Prints the number of GPU devices (two in an NC12 VM).
- That's it. Install any other stuff needed in the env; follow steps in the python repo guidance doc to find any software required in all conda envs. Just make sure no further installations attempt to change the versions of tensorflow, cudatoolkit or cudnn installed.

### Keras

- Any keras setup instructions?

## Deep learning setup in R

Add steps to get DL technologies working in R. Should be easier than with Python.
