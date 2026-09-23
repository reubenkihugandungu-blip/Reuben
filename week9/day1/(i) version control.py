# Definition

# Version control is a system that records every change made to a file or set of files over time. 
# It lets you view the full history of a project, revert to any previous state,
#  and work on multiple versions in parallel without conflict.

# Git is the most widely used version control system. 
# GitHub is a platform for storing Git repositories online and collaborating on them.
#  Git runs on your machine. GitHub runs in the cloud. They work together but are separate tools.

# Tool	                 What it is	                                              Where it runs
# Git	                 Version control software	                              Your computer (local)
# GitHub	             Hosting platform for Git repositories	                  Cloud (remote)
# Repository (repo)	     A project folder tracked by Git	                      Both local and remote
# Commit	             A saved snapshot of your project at a point in time	  Local first, then pushed

# Installing GIT

# git --version
# git version 2.44.0


# If you see a version number, Git is already installed. If the command is not found, download Git from git-scm.com and install it. Accept all defaults during installation.

# Operating System	                     Install method
# Windows	                             Download installer from git-scm.com
# macOS	                                 brew install git or install Xcode Command Line Tools
# Ubuntu / Debian	                     sudo apt install git

# First-Time Configuration
# Before making your first commit, tell Git who you are. 
# This information is attached to every commit you make. You only set this once per machine.

# Terminal: Set your identity

# Replace with your name and email
git config --global user.name "Brian Otieno"
git config --global user.email "brian@example.com"

# Set VS Code as the default editor
git config --global core.editor "code --wait"

# Verify your settings

 git config --global --list
# user.name=Brian Otieno
# user.email=brian@example.com
# core.editor=code --wait

# Tip: 
# Use the same email address for Git configuration and for your GitHub account.
# This links your commits to your GitHub profile and builds your contribution graph over time.
