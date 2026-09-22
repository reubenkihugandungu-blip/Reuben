# What is requirements.txt?

# requirements.txt is a plain text file that lists all the packages your project depends on, 
# along with their version numbers. It is how you share your project's dependencies with other 
# developers (or with a server) without sharing the actual installed files.

# You generate it automatically from your active environment with one command:

# With your venv activated, run:

pip freeze > requirements.txt

# This creates a file that looks like:
certifi==2024.2.2
charset-normalizer==3.3.2
openai==1.12.0
pandas==2.2.1
requests==2.31.0

# When someone else clones your project or you move it to a server, they recreate your exact
#  environment with one command:

# Create a new venv, activate it, then run:

pip install -r requirements.txt

# This installs every package at exactly the version you specified.
#  Your project works the same on their machine as it does on yours.

# The workflow in summary: Create venv. Activate. Install packages. Run pip freeze > requirements.txt.
#  Add venv/ to .gitignore. Push your code. Anyone who pulls it runs pip install -r requirements.txt 
# and they are ready.