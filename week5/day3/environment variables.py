# An environment variable is a value stored in your operating system, separate from your code.
# Your script reads it at runtime. The key never appears in your file.

# In Terminal (MAC/Linux) - temporary, lasts the session
export OPEN_API_KEY="sk-abc123yourrealkeyhere"

# In Command prompt (windows) - temporary
set OPEN_API_KEY=sk-abc123yourrealkeyhere

# os is a built-in Python module that lets your code interact with the operating system. 
# You do not install it with pip because it is part of Python's standard library.
#  import os gives you access to os.environ, a dictionary of all environment
#  variables currently set on your system, and os.getenv("KEY"), a function that retrieves a single variable by name. 
# This is how your Python script reads values that were set outside the script, such as keys stored in a .env file.