# Put all settings at the top of the script. Do not scatter URL strings and limit values throughout your code.
#  When something needs to change, you change it in one place.
# Configuration Block
import os

# Configuration
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
DEFAULT_CITY = "Nairobi"
STEP_GOAL = 10000
MAX_RESULTS = 50

print("Configuration loaded:")
print(f" Base URL: {BASE_URL}")
print(f" API Key: {API_KEY[:8]}...")
print(f" City: {DEFAULT_CITY}")
print(f"Step Goal: {STEP_GOAL:,}")
print(f" Max Results: {MAX_RESULTS}")

