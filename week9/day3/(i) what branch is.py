# A branch is a lightweight pointer to a specific commit.
#  When you create a branch, Git creates a new pointer at the current commit.
#  From that point, commits on the new branch and commits on the original branch diverge independently.
#  Neither branch affects the other until you merge them.

# Known example: The SMP program runs its standard protocol for existing members.
#  When testing a new protocol for a new cohort, you run it in parallel without changing what current members experience.
#  Once the new protocol proves effective, you fold its changes into the main program. That is branching and merging.

main ----o----o----o-----------o---> (after merge)
              \
               feature --o--o--o--/ (branch merged in)

# main stays untouched while feature work happens on its own line. 
# After merge, feature commits become part of main's history.
