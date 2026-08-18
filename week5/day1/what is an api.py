# An API (Application Programming Interface) 
# is a set of rules that lets one program request data or actions from another program over a network. 
# Your code sends a request to an API endpoint (a URL), and the API sends back a response, usually as JSON.

# An API has three core parts. The endpoint is the URL you send your request to.
#  The request is the message you send, including what you want and any parameters. 
# The response is what comes back, usually JSON data along with a status code.

# APIs communicate over HTTP, the same protocol browsers use. The method tells the API what action to take.

# Method	What It Does	                      Example
# GET	    Retrieve data	                     Fetch today's step count
# POST	    Send data to create something	     Log a new workout session
# PUT	    Update an existing record	          Update  today's sleep hours
# DELETE	Remove a record	Delete a duplicate   log entry

# Status codes
# Every API response includes a status code. The code tells you what happened before you even look at the data.

# Code	Meaning
# 200	OK. Request succeeded. Data is in the response.
# 201	Created. Your POST successfully created a new record.
# 400	Bad request. Your request had an error (wrong parameter, missing field).
# 401	Unauthorized. You need an API key or your key is wrong.
# 404	Not found. That endpoint or resource does not exist.
# 500	Server error. The API has a problem on its end.

# Always check the status code first. A 200 means your data is there.
#  Anything else and you need to investigate before trying to use the response body.

# What the requests Library Does
# requests is a third-party Python library that handles HTTP communication. 
# It is not built into Python, so you install it once with pip install requests. 
# After that, one line of code sends a request to any API endpoint in the world and 
# returns a response object containing the status code, headers, and the data body. 
# It is the most widely used HTTP library in Python and the standard starting point for anyone working with APIs.