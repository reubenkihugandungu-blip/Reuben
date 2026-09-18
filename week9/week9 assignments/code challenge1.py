# Code Challenge
# You have a list of commit messages. Use a for loop with enumerate to print each one numbered.
#  Your output must match exactly:

# Use this list:

commits = [
    "Initial commit",
    "Add SMP tracker script",
    "Fix loop logic in day5.py",
    "Add requirements.txt"
]

for number, commit in enumerate(commits, start=1):
    print(f"{number}. {commit}")

