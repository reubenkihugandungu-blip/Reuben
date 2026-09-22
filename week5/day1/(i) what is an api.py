# Every app you use pulls live data from somewhere. Weather apps fetch forecasts. 
# Fitness trackers sync stats. Payment platforms check balances. 
# The mechanism behind all of it is an API.
# This week you go from working with local files to pulling data from the internet.

# An API (Application Programming Interface) 
# is a set of rules that lets one program request data or actions from another program over a network. 
# Your code sends a request to an API endpoint (a URL), and the API sends back a response, usually as JSON.

# Think of a phone repair shop counter.
# You walk in and hand over your phone. 
# You tell the person at the counter what you need: screen replacement, battery swap. 
# They go into the workshop, get it done, and bring back the result.
# You never go into the workshop yourself. The counter is the API. 
# It is a defined interface between you and the system doing the work.
# You send a request. You get back a response.

# An API has three core parts. The endpoint is the URL you send your request to.
# The request is the message you send, including what you want and any parameters. 
# The response is what comes back, usually JSON data along with a status code.

## HTTP Methods

# APIs communicate over HTTP, the same protocol browsers use.
#  The method tells the API what action to take.

# The first package you will install for this course is requests.
# It is the standard library for making HTTP calls in Python. 
# Calling an API means sending an HTTP request and reading the response.
# requests handles all of that with a clean, readable syntax.

# Method	What It Does	                      Example
# GET	    Retrieve data	                     Fetch today's step count
# POST	    Send data to create something	     Log a new workout session
# PUT	    Update an existing record	          Update  today's sleep hours
# DELETE	Remove a record	Delete a duplicate   log entry

## Status codes
# Every API response includes a status code. 
# The code tells you what happened before you even look at the data.

# Code	Meaning
# 200	OK. Request succeeded. Data is in the response.
# 201	Created. Your POST successfully created a new record.
# 400	Bad request. Your request had an error (wrong parameter, missing field).
# 401	Unauthorized. You need an API key or your key is wrong.
# 404	Not found. That endpoint or resource does not exist.
# 500	Server error. The API has a problem on its end.

# Always check the status code first. A 200 means your data is there.
#  Anything else and you need to investigate before trying to use the response body.

