# Create a new repository on GitHub. 
# Go to github.com, click the + icon, then "New repository." Name it, leave it empty (no README, no .gitignore),
#  and click Create. GitHub gives you a URL like git@github.com:username/repo-name.git

# In your local project, add GitHub as the remote origin: git remote add origin git@github.com:username/smp-tracker.git

# Push your local main branch to GitHub: git push -u origin main. The -u flag links your local main to the remote main. 
# After this first push, you only need git push.

# Terminal: Push to GitHub for the first time

# Add the remote (replace URL with yours from GitHub)
git remote add origin git@github.com:brianotieno/smp-tracker.git

# Confirm the remote is set
git remote -v
origin  git@github.com:brianotieno/smp-tracker.git (fetch)
origin  git@github.com:brianotieno/smp-tracker.git (push)

# Push main branch and set upstream
git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 842 bytes | 842.00 KiB/s, done.
Branch 'main' set up to track remote branch 'main' from 'origin'.
 * [new branch]      main -> origin/main