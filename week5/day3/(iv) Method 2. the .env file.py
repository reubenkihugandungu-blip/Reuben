# The .env File (Recommended)

# A .env file stores key-value pairs in a text file in your project folder. 
# You load it at runtime using the python-dotenv library.
#  The file stays on your machine and never gets pushed to GitHub.

# Its the recommeded method.

# .env file (in your project root)

SMP_API_KEY=smp_live_abc123xyz
OPENAI_API_KEY=sk-proj-abc123yourkey
WEATHER_API_KEY=wth_abc456yourkey

# .gitignore (also in your project root)
.env

pip install python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()   # reads .env and sets environment variables

api_key = os.getenv("SMP_API_KEY")
print(api_key)

# Add .env to your .gitignore before your first commit. 
# Once a key is in your git history, rotating (replacing) the key is the only fix.
# Prevention is a one-line addition to .gitignore.