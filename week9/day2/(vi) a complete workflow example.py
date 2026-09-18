# 1. Check current state
git status
On branch main
Changes not staged for commit:
        modified:   tracker.py
Untracked files:
        api_client.py

# 2. Stage both files
git add tracker.py api_client.py

# 3. Verify what is staged
git status
On branch main
Changes to be committed:
        modified:   tracker.py
        new file:   api_client.py

# 4. Commit
git commit -m "Add API client module and fix tracker null check"
[main f1e2d3c] Add API client module and fix tracker null check
 2 files changed, 47 insertions(+), 1 deletion(-)

# 5. Confirm clean state
git status
On branch main
nothing to commit, working tree clean

# 6. View history
git log --oneline
f1e2d3c Add API client module and fix tracker null check
d4e5f6a Add weekly summary report to dashboard
a1b2c3d Add SMP tracker script with daily check-in logic

# Try This:
# In your smp-tracker project from Day 41, create three files: 
# tracker.py, README.md, and .gitignore.
# Write one line in each. Stage and commit them all in a single commit.
#  Then edit tracker.py and make a second commit with only that change.
#  Run git log --oneline and verify you see two separate commits.