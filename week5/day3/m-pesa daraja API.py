# The same authentication pattern applies to every business API in Kenya. The Safaricom M-Pesa Daraja
#  API requires a Consumer Key and Consumer Secret. You exchange them for a Bearer token, 
# then use that token on every transaction call. 
# Farms, agro-dealers, and small businesses that accept M-Pesa payments build on top of this exact flow.

# Simulate M-PESA Daraja Auth flow
import os
import base64

# Step 1: Load credentials from environment (never hardcode)
os.environ["MPESA_CONSUMER_KEY"] = "demo_consumer_key_abc123"
os.environ["MPESA_CONSUMER_SECRET"] = "demo_secret_xyz789"

consumer_key  = os.getenv("MPESA_CONSUMER_KEY")
consumer_key = os.getenv("MPESA_CONSUMER_SECRET")

# Step 2: Encode credentials (Daraja requires Base64)
credentials = f"{consumer_key}:{consumer_key}"
encoded = base64.b64encode(credentials.encode()).decode()

#Step 3: In production you POST this to Daraja to get a token:
