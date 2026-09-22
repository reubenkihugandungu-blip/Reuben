# Virtual environments

# You have been writing Python scripts and installing packages with pip. 
# So far you have installed everything in one place, and it works. 
# But as your projects grow and multiply, installing everything in the same place causes problems. 
# Virtual environments solve this. Every professional Python project uses one.

# The Problem with Installing Everything Globally
# When you run pip install requests without any setup, the package gets installed globally 
# on your computer. That means every Python project on your machine shares the same packages. 
# This sounds convenient until two projects need different versions of the same package.

# Imagine this scenario: your first project needs pandas version 1.5. 
# Your second project needs pandas version 2.1. They cannot both be installed globally at the same time.
#  One project breaks. 
# This is called a dependency conflict, and it is one of the most common sources of errors for
#  developers who do not use virtual environments.

# What a Virtual Environment Is

# A virtual environment is a self-contained folder on your computer that holds its own copy of Python
#  and its own set of installed packages.
#  When you activate it, any packages you install go into that folder only,
#  not into the global Python installation. Different projects get different environments, 
# so they never interfere with each other.

# Creating and Using a Virtual Environment

# Python comes with the venv tool built in.
#  You create a virtual environment once per project, activate it, and then install packages inside it.

# 1 : Create the environment
# Navigate to your project folder in the terminal, then run:

python -m venv venv

# This creates a folder called venv inside your project. That folder is the environment.

# 2 : Activate it
# Windows (Command Prompt or PowerShell)

venv\Scripts\activate

# Mac or Linux
source venv/bin/activate

# When activated, your terminal prompt changes to show (venv) at the start. 
# That means you are inside the environment.

# 3 : Install packages inside it

pip install requests pandas openai

# These packages go into your venv folder only. Your global Python stays clean.

# 4 : Deactivate when done

deactivate

# Your terminal returns to normal. The packages are still in the venv folder, ready for next time.
# Activate every time you open a new terminal for that project.

#  The environment does not stay active between terminal sessions.
#  Opening a new terminal window means running the activate command again before you run your scripts.

# Never commit your venv folder to GitHub.
# The venv folder can be hundreds of megabytes. It contains binary files specific to your operating 
# system. Always add venv/ to your .gitignore file so it never gets pushed. 
# Other developers recreate their own environment from your requirements.txt instead.