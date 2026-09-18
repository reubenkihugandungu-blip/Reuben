# A pull request (PR) is a GitHub feature, not a Git command. 
# It is a request to merge one branch into another, reviewed on GitHub's interface. 
# You push a feature branch to GitHub, then open a PR from that branch into main.
#  The PR shows the diff, allows comments, and records the merge decision.

# The pull request workflow is the standard for team collaboration and for contributing to open source projects:

# Create a feature branch locally: git switch -c feature/step-prediction

# Do the work, commit it.

# Push the branch to GitHub: git push -u origin feature/step-prediction

# On GitHub, click "Compare & pull request." Write a description, then click "Create pull request."

# Review the diff. If all good, click "Merge pull request." The branch is merged into main on GitHub.

# Pull the merge back locally: git switch main then git pull.
#  Delete the local feature branch: git branch -d feature/step-prediction.

# Try This:
# Create a new repository on GitHub called smp-tracker. 
# Connect your local smp-tracker project to it with git remote add origin. Push all commits with git push -u origin main.
#  Refresh the GitHub page and confirm your files and commit history appear.