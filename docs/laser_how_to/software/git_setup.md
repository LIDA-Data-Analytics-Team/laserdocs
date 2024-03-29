---
layout: default
title: Using Git
parent: Install & Use Software
grand_parent: LASER How To
nav_order: 2
---

# Setting up Git for Version Control

To use Git for version control in a LASER VRE, first check Git has been installed via [Software Center](./index.html). Once installed, you'll need to change Git's home directory and configure your own user name and email address. Your name and email are needed to identify who has committed changes to code. You'll need to do this only once.

Open Git Bash to begin.

# Change Git home directory

Git Bash will open to your home directory, which by default will be `M:\`. You'll need to change the home directory to your user-specific folder on the C: drive.

Run the following command, replacing `<username>` with your UoL username:<br>
`setx HOME C:/Users/<username>`

You should see a message confirming you successfully changed the home directory.

![Screenshot of git bash illustrating success after setting your home directory](../../../images/git_setup/02_set_home_path.PNG){:width="70%" .mx-auto}

Now close and reopen Git Bash to refresh your settings. It should reopen to your new home directory. You can check using `pwd`.

![Screenshot of git bash illustrating the new default working directory](../../../images/git_setup/03_check_home_path.PNG){:width="70%" .mx-auto}

When you make changes to your user configurations, they will be saved to your new home directory.

# Update user config

To identify yourself when you commit changes to code, declare your user name and email in a gitconfig file. These configurations get used automatically when versioning your code.

Run the following commands in Git Bash:<br>
`git config --global user.name <your-name>`<br>
`git config --global user.email <your-email>`

This will create a file called .gitconfig in your home directory, or add to the file if it already exists. From your home directory in Git Bash, check the contents of .gitconfig using `cat .gitconfig`.

![Screenshot of git bash illustrating how to set global config for user name and user email](../../../images/git_setup/04_set_user_config.PNG){:width="70%" .mx-auto}

# Using Git

You can then use Git as you would normally on another machine. **We strongly recommend you always store your Git repositories and all other files in your project shared storage** (`N:\`). Navigate to your shared storage and initialise a Git repository like so:

![Screenshot of git bash illustrating how to initialise a git repo in the VRE shared storage](../../../images/git_setup/05_git_init.PNG){:width="70%" .mx-auto}
