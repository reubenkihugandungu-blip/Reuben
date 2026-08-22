# When authentication fails, the API returns a 401 or 403 status code.
#  Always check the status before trying to use the response body.

# Handling Auth errors
def handle_api_response(status_code, body): # defines a function named handle api response
    if status_code == 200:# is the HTTP response status, such as 200
        return body # is the data returned by the API
    elif status_code == 403: # the key is recognized but does not have the permission to access the endpoint
        raise PermissionError("Acces denied. Your key does not have permission for this endpoint.")
    elif status_code == 429:
        raise RuntimeError("Rate limit exceeded. Wait before retrying.")
    elif status_code >= 500: # the problem is probably on the server
        raise RuntimeError(f"Server error ({status_code}). Try again later.")
    else:
        raise RuntimeError(f"Unexpected status: {status_code}")
    
# Test with different status codes
test_cases = [
    (200, {"members": [{"name": "James Omondi"}]}),# a successfull response containing a list of members
    (401, {"error": "invalid key"}),# a response showing that the API key is invalid
    (429, {"error": "rate_limit_exceeded"}),
    (500, {"error": "internal_server_error"}),
]

for status, body in test_cases:# loops through every test case, for each tuple status receives the status code
    try:                       # body receives the response data, try starts a block where python will attempt to run code tehat might produce an error
        result = handle_api_response(status, body)# calls the function using the current status and response body
        print(f"Status {status}: OK, got {result}")
# 👇catches any exception raised inside the try block. Exception means a general python error
# as e stores the error in the variable e
    except Exception as e:
        print(f"Status {status}: {e}")