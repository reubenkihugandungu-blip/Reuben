# Definition
# git add moves files from the working directory into the staging area. 
# The staging area is a preparation zone. You choose exactly which changes go into the next commit.
#  Files in the staging area are described as "staged" or "indexed."

# Known example: Packing a box to ship. Your desk is covered with items (working directory).
#  You pick up specific items and place them in the box (staging area).
#  When the box is sealed and labeled, that is the commit.
#  You do not have to put everything on the desk into one box.

# Stage a single file
git add tracker.py

# Stage multiple specific files
git add tracker.py config.py README.md

# Stage all changes in the current directory
git add .

# Check what is staged
git status
On branch main

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   tracker.py
# Tip:
#  git add . stages everything that is not in .gitignore. It is fast but imprecise. 
# Use git add filename when you want to separate unrelated changes into different commits. 
# One commit should represent one logical change.