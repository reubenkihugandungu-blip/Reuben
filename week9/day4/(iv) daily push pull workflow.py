# Terminal: Day-to-day remote workflow

# Start of work: pull any remote changes (important on shared repos)
git pull
Already up to date.

# Do your work, stage, commit as normal
git add .
git commit -m "Add daily step trend calculation"

# Push to GitHub
git push
Enumerating objects: 5, done.
To git@github.com:brianotieno/smp-tracker.git
   3c4d5e6..7f8a9b0  main -> origin/main

# Push a feature branch to GitHub
git push -u origin feature/coaching-module
Branch 'feature/coaching-module' set up to track remote branch 'feature/coaching-module' from 'origin'.
 * [new branch]      feature/coaching-module -> origin/feature/coaching-module