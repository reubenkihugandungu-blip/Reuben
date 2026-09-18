# BRANCHING LOGIC

# Simulate a branching workflow in Python
branches = {"main": ["initial commit", "add README"], "feature": ["add login page"]}

current = "main"
print(f"On branch: {current}")
for commit in branches[current]:
    print(f"  {commit}")