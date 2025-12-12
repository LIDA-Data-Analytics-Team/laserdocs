---
nav_exclude: true
---
## Creating Conda Environments for LASER VREs

- Warning: Creating environments (envs) and installing modules takes much longer in DAT02 than it would on your laptop
- Log in to LASER > DAT Data Transfer Service
- open p: drive; create a project folder (if not existing)
- Open anaconda prompt
- Store conda envs on P:\ in a project-specific folder. E.g., create a VRE folder, then create an env in it using the conda create command, including any basic software you want to add during creation.<br>`conda create -p P:\V0000\V0000_env_00 python=3.8`
- As long as envs are stored in VRE folders, the envs could be named whatever the researcher chooses. However, in the absence of researcher choice, a naming convention might be useful? Such as, `<vre-id>_env_<env-id>`, where env-id is two chars, starting at 00 and counting up. If the env is specific to a VM, e.g. one that contains a GPU, then maybe use the VM ID in the env name? You may have better ideas though.
- The following modules should always be added to any conda env:
	- spyder-kernels: Currently you need to install a version >=1.9.1 & < 1.10. I recommend 1.9.4<br>`conda install spyder-kernels=1.9.4`
	- Spyder: Version >= 4.1 is recommended.<br>`conda install spyder=4.1.5`
	- ipykernel (this comes with spyder-kernels so no extra install needed)
	- Latest Jupyter `conda install jupyter`
	    - To run a notebook using their conda env, users will need to install an ipython kernel by running:<br>`ipython kernel install --user --name=<env-name>`
	    - This last instruction is on the LASER Docs site, users can do it. Just mentioning it here, because if a user is struggling to get Jupyter Notebook working, they may have missed this step.
- Whenever you create or update an env, **always** export a new requirements version using<br>`conda env export > P:\_requirements\<vre-folder>\<env-name>.yml`
- Then version control the .yml file. The _requirements/ folder is a git repo. You can find a portable version of git bash at `\\azlrdprepos.file.core.windows.net\packages\PortableGit\`

### Snippets  

Iterate through each entry in requirements.txt and conda install modules and dependancies and pip install if no conda available (Windows)  
```python
FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f" || pip install "%f"
```
