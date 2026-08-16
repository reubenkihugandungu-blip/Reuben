import json, tempfile
# Save a list of 3 students (name, score) to JSON
# Read it back and print only students who scored above 70

students = [
    {"name": "Eric", "score": 85},
    {"name": "James", "score": 62},
    {"name": "Amina", "score": 91}
]
path = tempfile.mktemp(suffix='.json')
with open(path, 'w') as f:
    json.dump(students, f)
with open(path) as f:
    loaded = json.load(f)
    for s in loaded:
        if s['score'] > 70:
            print(f"{s['name']}: {s['score']}")