# A merge conflict happens when two branches both changed the same line of the same file.
#  Git cannot decide automatically which version is correct. 
# It pauses the merge and marks the conflicting sections in the file with conflict markers.
#  You resolve the conflict by editing the file manually, then committing.

# Inside tracker.py after a conflict, Git inserts markers:

<<<<<<< HEAD
def assess_day(steps):
    return steps >= 10000
=======
def assess_day(steps, goal=10000):
    return steps >= goal
>>>>>>> feature/flexible-goal

# HEAD = your current branch (main)
# Everything between === and >>> = the incoming branch changes
# Decision: pick one, combine both, or write something new
# Then delete all marker lines and save

# Terminal: Resolving a conflict

# Git shows the conflict
git merge feature/flexible-goal
Auto-merging tracker.py
CONFLICT (content): Merge conflict in tracker.py
Automatic merge failed; fix conflicts and then commit the result.

# Open the file, edit it, remove conflict markers, save
code tracker.py

# After resolving: stage the file
git add tracker.py

# Complete the merge with a commit
git commit -m "Merge feature/flexible-goal: add configurable goal parameter"
[main 7a8b9c0] Merge feature/flexible-goal: add configurable goal parameter

# Tip: VS Code has a built-in merge conflict editor.
#  When a conflicted file is open, VS Code shows buttons above each conflict section: 
# "Accept Current Change," "Accept Incoming Change," "Accept Both Changes," and "Compare Changes."
#  These buttons edit and clean the file for you. Use them instead of manually removing markers.