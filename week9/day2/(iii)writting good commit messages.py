# Writing Good Commit Messages
# A commit message is the only communication between you-now and you-in-six-months.
#  Write it for someone who knows the project but has no idea what you just changed or why.

# Format rule                     	   Good example	                                   Bad example
# Start with a verb (imperative)	   Add member check-in endpoint	              Added some stuff to the API
# Under 72 characters for the title	   Fix null error in goal calculation	      Fixed that bug where it crashes
# No full stop at the end of title	   Update .gitignore to exclude .env	      Update .gitignore to exclude .env.
# Present tense, not past tense	       Remove duplicate validation check	      Removed duplicate validation check
# Explain why, not just what	       Use median instead of mean (skewed data)	  Change mean to median

# Note: For a longer explanation, leave the -m flag off.
#  Git opens the editor (VS Code if configured). The first line is the summary. Leave a blank line.
#  Write the full explanation below. This is called a multi-line commit message.