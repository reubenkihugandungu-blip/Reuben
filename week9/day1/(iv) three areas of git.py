# Git tracks files across three areas. Understanding these three areas is the key to understanding every Git command.

# Area	                         What it contains	                                How to interact
# Working directory	       All files as they currently exist on disk	             Edit in VS Code as normal
# Staging area (index)	   Files selected for the next commit	                     git add filename
# Repository (.git)     	All commits and complete history	                     git commit -m "message"

# Try This:

# Open a terminal in VS Code. Navigate to any project folder and run git init.
#  Create a file called notes.txt, write one line in it, and save. Run git status. 
# Notice that the file appears as "Untracked." This is Git seeing the file but not yet recording it.

# Common Setup Commands Summary

# Command                               	What it does	                        When to use
# git --version	                         Check installed version	                Verify Git is installed
# git config --global user.name "..."	Set your display name	                     Once per machine
# git config --global user.email "..."	Set your email	                             Once per machine
# git init	                            Create a new local repository	             Start of every project
# git status	                        See tracked/untracked/staged files	         After every action
# touch .gitignore	                    Create the ignore file	                     Right after git init

# Same Concept, Different Context: 
# A Jua Kali phone repair technician who keeps a written log of every repair (date, device, fault, fix) 
# has a manual version of what Git does. Each log entry is a commit. git init starts the logbook.
#  git add marks which changes go into the next entry.
#  git commit writes the entry permanently with a message you can read back months later.