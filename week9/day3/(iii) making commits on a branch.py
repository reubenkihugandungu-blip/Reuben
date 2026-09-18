# Commits on a branch are completely isolated from other branches.
#  The files on disk change when you switch branches. Git swaps the files out automatically.

# Start on main, create feature branch
git switch -c feature/coaching-module

# Create a new file on this branch
touch coaching.py
echo "def get_coaching(sleep, water, steps): pass" > coaching.py

# Stage and commit on the feature branch
git add coaching.py
git commit -m "Add coaching module skeleton"
[feature/coaching-module 3c4d5e6] Add coaching module skeleton
 1 file changed, 1 insertion(+)

# Switch back to main
git switch main

# coaching.py does not exist on main
ls
README.md  tracker.py  .gitignore

# Switch back to feature branch - coaching.py reappears
git switch feature/coaching-module
ls
README.md  coaching.py  tracker.py  .gitignore