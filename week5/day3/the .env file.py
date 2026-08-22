# A .env file stores key-value pairs in a text file in your project folder. 
# You load it at runtime using the python-dotenv library.
#  The file stays on your machine and never gets pushed to GitHub.
# Its the recommeded method.

from dotenv import load_dotenv
import os

load_dotenv() # reads .env and sets environment variables

api_key = os.getenv("SMP_API_KEY")
print(api_key)