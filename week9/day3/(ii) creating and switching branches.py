# # See all branches (current branch marked with *)
git branch
* main

# Create a new branch
git branch feature/api-dashboard

# Switch to it
git switch feature/api-dashboard
Switched to branch 'feature/api-dashboard'

# Create AND switch in one command (preferred)
git switch -c feature/coaching-module
Switched to a new branch 'feature/coaching-module'

# Confirm current branch
git branch
  feature/api-dashboard
* feature/coaching-module
  main

# Switch back to main
git switch main

# Tip: Use a naming convention for branches.
#  Common patterns are feature/description for new features, fix/description for bug fixes,
#  and chore/description for non-code tasks like updating dependencies. 
# Consistent names make it clear what each branch is for before you even open it.
