# Commands Reference

# Command	                                     Purpose
# git add .	                                  Stage all changes
# git add                                     filename	Stage one file
# git commit -m "msg"	                      Commit staged changes
# git commit -am "msg"	                      Stage tracked files and commit in one step
# git log	                                  Full commit history
# git log --oneline	                          Compact history, one line per commit
# git diff	                                  Unstaged changes
# git diff --staged	                          Staged changes
# git show <hash>	                          Full diff of a specific commit
# git restore filename	                      Discard working-directory edits
# git restore --staged filename            	  Unstage a file

# Same Concept, Different Context: 
# A dairy farmer who records weekly milk yield per cow selects which rows to enter first (staging),
#  then writes them into the permanent record book (commit).
#  Git log is that record book: every entry is timestamped, permanent, and readable.
#  git diff is the farmer comparing this week's yield against last week's entry.