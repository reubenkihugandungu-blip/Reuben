# GIT COMMANDS

# Git is a terminal tool, not Python.
# Use this terminal to review the logic behind each command.

# Simulate tracking changes
changes = []
changes.append("Created hello.py")
changes.append("Added user input")
changes.append("Fixed loop bug")

for i, msg in enumerate(changes, 1):
    print(f"commit {i}: {msg}")