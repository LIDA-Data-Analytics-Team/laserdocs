---
layout: page
---

## Using Python in LASER

Python is distributed to LASER users via Anaconda, a distribution of several scientific computing technologies. Anaconda contains out of the box a version of Python and many of the most popular modules in data science and research. This basic installation is called its base environment.

Environments encapsulate the software dependencies of your project's code, making your project more reproducible. Conda environments are Anaconda's answer to Python virtual environments (much like pipenv).

There is no internet connection in the VREs needed to create your own environments. Instead, any Python modules that you need can be provided in bespoke environments. Contact the [LIDA Data Analytics Team](mailto:ircdst@leeds.ac.uk) to request new Python modules and they will be added to your project's environment. (We can provide the same environments for R, if you like - but, see also the [R repository](install-r-package.md)).

All bespoke conda environments are stored in LASER's Python repository, on the `P:\` drive. Within the Python repo, you'll find a subfolder for your VRE (e.g., V0001), containing all your requested environments.

Details follow on how to use conda environments in various ways.

### Using conda at the command line

- Open Anaconda Prompt (cmd) from the Start menu by typing anaconda in the search bar and selecting it from the results.
![01_open_conda.png](images/using_python/01_open_conda.png)
- Activate your conda environment by passing the full path to your environment stored in the Python repo. E.g.:
`conda activate P:\_demo\demo_env`
![02_activate_env.png](images/using_python/02_activate_env.png)
- You should then see the name of your conda environment in the prompt, shown in parentheses where it previously said "base".
- You can check that the environment contains the software you need by running `conda list`.
![03_list_env.png](images/using_python/03_list_env.png)
- Run Python code in the command line using the `python` command, like you normally would.
- Use this environment as you would use any other. Instructions on how to use your environment in various Python IDEs are below.
- To deactivate the environment, type:
`conda deactivate`

### Using conda in Spyder

- Activate your conda environment at the command line following instructions above.
- Type `spyder` to load Spyder using your environment.
- Spyder will then have access to all the modules and dependencies for your project. Create Spyder projects and use as you normally would.
- To check Spyder is correctly using your environment, hover over the name of the active Python interpreter in the bottom status bar and the file path that appears should show the python.exe within your environment
![04_spyder_confirm_env.png](images/using_python/04_spyder_confirm_env.png)

### Using conda in Jupyter Notebook

- Activate your conda environment at the command line.
- The first time you want use your environment in a jupyter book, you'll first need to install an ipython kernel by running
`ipython kernel install --user --name=<env-name>`
Where <env-name> can be replaced with a name of your choice. We recommend you use the same name as your environment, but not the full path (i.e., for environment at P:\_demo\demo_env name your ipython kernel demo_env).
- You won't need to install a new kernel in future
- Type `jupyter notebook` to load Jupyter using your environment.
- Jupyter Notebook will open.
- Navigate to a folder where you want to create a new notebook
- Click New and then select your environment's kernel from the dropdown.
![05_jupyter_kernel.png](images/using_python/05_jupyter_kernel.png)
- A new notebook will open, which will have access to all the software in your environment.
- Check your notebook is using the right kernel by looking at the kernel name in the top right.
![06_jupyter_kernel_confirmed.png](images/using_python/06_jupyter_kernel_confirmed.png)
