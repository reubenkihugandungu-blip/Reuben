# PARSING JSON

import json
# Parse this nested JSON and print the author and title
response = '{"book": {"title": "Clean Code", "author": "Robert Martin", "year": 2008}}'
data = json.loads(response) # converting data to a python dict
book = data["book"] # navigating layer by layer by storing dict item(book) in a variable book
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")