# Definition
# .gitignore is a plain text file in the root of your project.
# Each line specifies a file pattern that Git should ignore.
#  Files matched by .gitignore are never tracked, never staged, and never committed,
#  even if they are inside the project folder.

# Known example: A workshop intake sheet that has a "Do not log" column. 
# Some items go through the workshop but never appear in the repair log: cleaning supplies,
#  broken tools being discarded. .gitignore works the same way.
#  It specifies what goes through the project but never into the version history.

# In VS Code
# File: .gitignore

# Python
__pycache__/
*.pyc
*.pyo
.env
venv/
.venv/

# Environment variables
.env
.env.local

# Data files with sensitive content
*.csv
secrets.json

# OS files
.DS_Store
Thumbs.db

# VS Code settings
.vscode/

# Terminal: Create .gitignore and verify it works
# Create the .gitignore file
touch .gitignore

# Open it in VS Code and add patterns, then save
code .gitignore

# Create a file that should be ignored
touch .env

# Check status - .env should not appear
git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

# nothing added to commit but untracked files present

# .env is not listed because .gitignore hides it
# Tip:
#  Never commit a .env file. It contains API keys and database passwords. 
# If you accidentally commit one, treat those credentials as compromised and rotate them immediately.
#  Add .env to .gitignore before creating the file, not after.
