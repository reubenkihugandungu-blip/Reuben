# pip in Practice: Installing Packages for Your Projects

# Installing requests
# Calling an API means sending an HTTP request and reading the response. 
# requests handles all of that with a clean, readable syntax.

## Open your terminal and run:

pip install requests

# Tip: If you are using a virtual environment (which you should be from Week 5 onward),
#  make sure it is activated before running pip install.
#  Check that your terminal prompt shows (venv) at the start.

# Verifying an Installation
# After installing, confirm it worked with:

pip show requests

# All the pip commands you need
# Command	                                           What it does
# pip install requests	                        Install the latest version of a package
# pip install requests==2.28.0	                Install a specific version (pin the version)
# pip install --upgrade requests	            Upgrade an already-installed package to latest
# pip uninstall requests	                    Remove a package
# pip list	                                    Show all installed packages and their versions
# pip show requests	                            Show details about one installed package
# pip freeze	                               Print all installed packages in requirements format
# pip freeze > requirements.txt	               Save your current environment to a file
# pip install -r requirements.txt	            Install everything listed in requirements.txt

# Installing Multiple Packages at Once
# You can install several packages in one command:

pip install requests python-dotenv pandas

# Or for a new project, install everything from a requirements file at once:

pip install -r requirements.txt

# This is how you set up any project someone else built. Clone the repo, activate a fresh venv, 
# run this command, and the environment is ready.
