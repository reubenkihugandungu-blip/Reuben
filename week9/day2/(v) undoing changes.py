# Situation                                 Command	                                    What happens
# Discard unsaved edits in a file	   git restore filename	                   File reverts to last committed state
# Remove a file from staging	       git restore --staged filename	       File stays edited but leaves staging area
# Undo last commit (keep changes)	   git reset HEAD~1	                   Commit removed; changes back to working directory
# View old version of a file	       git show a1b2c3d:tracker.py	        Prints the file as it was at that commit

# Warning:
#  git reset --hard HEAD~1 
# permanently discards the last commit AND all its changes. There is no undo for this.
#  Use git reset HEAD~1 (without --hard) if you want to uncommit but keep your edits.