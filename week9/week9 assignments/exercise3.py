# MERGE SIMULATION

# Simulate merging a feature branch into main
branches = {
    "main": ["initial commit", "add README"],
    "feature": ["add login page", "add auth logic"]
}

# Merge feature into main
branches["main"].extend(branches["feature"])
print("After merge, main branch history:")
for commit in branches["main"]:
    print(f"  {commit}")