# Definition
# git commit takes everything in the staging area and saves it as a permanent snapshot in the repository.
#  Each commit gets a unique hash (a 40-character hex string), a timestamp, an author, and a message.

# Commit with an inline message
git commit -m "Add SMP tracker script with daily check-in logic"
[main (root-commit) a1b2c3d] Add SMP tracker script with daily check-in logic
 3 files changed, 84 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 tracker.py

# Stage and commit all tracked files in one step
git commit -am "Fix step count calculation off-by-one error"

# Note: -a only stages already-tracked files, not new files