# Branch	                      Purpose	                                  Rule
# main	                       Production-ready code at all times	     Never commit directly to main
# feature/x	                   One feature or change	                 Branch from main, merge back when done
# fix/x	                       Bug fix	                                 Branch from main, merge immediately after testing

# Try This:
# In your smp-tracker project, create a branch called feature/weekly-report. 
# On that branch, create a file called report.py and add two lines of code. Commit it. 
# Switch back to main and confirm report.py is gone. 
# Switch back to the feature branch and confirm it returns. Then merge the branch into main and delete the feature branch.