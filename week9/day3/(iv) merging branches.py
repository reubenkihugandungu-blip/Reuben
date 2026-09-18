# git merge takes the commits from one branch and applies them to another. You always merge INTO the current branch.
#  To merge a feature branch into main, switch to main first, then run git merge feature-branch-name.

# Merging a feature branch into main

# Step 1: Switch to main
git switch main
Switched to branch 'main'

# Step 2: Merge the feature branch
git merge feature/coaching-module
Updating a1b2c3d..3c4d5e6
Fast-forward
 coaching.py | 1 +
 1 file changed, 1 insertion(+)

# coaching.py is now on main
ls
README.md  coaching.py  tracker.py  .gitignore

# Step 3: Delete the feature branch (optional, keeps things clean)
git branch -d feature/coaching-module
Deleted branch feature/coaching-module (was 3c4d5e6).

# View merged history
git log --oneline
3c4d5e6 Add coaching module skeleton
f1e2d3c Add API client module and fix tracker null check
a1b2c3d Add SMP tracker script with daily check-in logic

# Note: Fast-forward merge happens when main has no new commits since the branch was created. 
# Git simply moves the main pointer forward to the tip of the feature branch. No merge commit is created.
#  The history stays linear.