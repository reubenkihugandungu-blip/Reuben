# Definition
# git log shows the full list of commits in the current branch, from newest to oldest.
#  Each entry shows the commit hash, author, date, and message.

# Full log
git log
commit d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3
Author: Brian Otieno <brian@example.com>
Date:   Wed Jul 15 09:22:14 2026 +0300

    Add weekly summary report to dashboard

commit a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b
Author: Brian Otieno <brian@example.com>
Date:   Tue Jul 14 17:45:01 2026 +0300

    Add SMP tracker script with daily check-in logic

# Compact one-line format
git log --oneline
d4e5f6a Add weekly summary report to dashboard
a1b2c3d Add SMP tracker script with daily check-in logic

# Show only last 5 commits
git log --oneline -5

# Show what changed in each commit
git log --stat

# The short hash (first 7 characters) is all you need to reference a commit in other commands.
#  Git is smart enough to find the full hash from the first few characters, as long as they are unique in the repository.

# Seeing What Changed
# Terminal: Diff commands
# Show unstaged changes (what you changed but have not yet added)

git diff
diff --git a/tracker.py b/tracker.py
index 3a4b5c6..7d8e9f0 100644
--- a/tracker.py
+++ b/tracker.py
@@ -12,7 +12,7 @@ def assess_day(steps):
-    return steps >= 10000
+    return steps >= 10000 and steps is not None

# Show staged changes (what is ready to commit)
git diff --staged

# Show all changes in a specific commit
git show a1b2c3d

# Compare two commits
git diff a1b2c3d d4e5f6a

# Tip: In diff output, lines starting with - were removed.
#  Lines starting with + were added. Lines with neither were unchanged context. 
# Green in most terminals = added. Red = removed.