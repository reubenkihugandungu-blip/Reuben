# git clone downloads a full copy of a remote repository to your machine, including all commits and branches. 
# It automatically sets the remote as "origin." Use this when starting work on a project that already exists on GitHub.

# Cloning a repo

# Clone via SSH (preferred if SSH is set up)
git clone git@github.com:brianotieno/smp-tracker.git
Cloning into 'smp-tracker'...
remote: Enumerating objects: 12, done.
Receiving objects: 100% (12/12), done.

# Clone via HTTPS (works without SSH setup)
git clone https://github.com/brianotieno/smp-tracker.git

# Clone into a specific folder name
git clone git@github.com:brianotieno/smp-tracker.git my-tracker