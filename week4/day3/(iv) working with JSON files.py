# In VS Code, you use json.dump() (no s) to write to a file and json.load() (no s) to read from one.
# The interactive terminals here simulate this using in-memory strings.

# writing JSON to a file (use in VS code):
with open("log.json", "w") as f:
    json.dump(daily_log, f, indent=2)

# Reading JSON from a file (use in vs code):
with open("log.json", "r") as f:
    data = json.load(f)