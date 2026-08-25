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
# url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?" grant_type=client_credentials"
# headers = {"Authorization": f"Basic {encoded}"}
# response = requests.get(url, headers=headers)
# token = response.json()["access_token"]

# Simulate the token response
simulated_token = "Q2xpZW50X0lENmJlYjA2NWEtMjA4Ny00OTU2"

print("Credentials encoded (Base64):", encoded[:20] + "...")
print()
print("Simulated token received:", simulated_token[:20] + "...")
print()
print("In production, pass this token to every M-Pesa API call:")
print(f' headers = {{"Authorization": "Bearer {simulated_token[:12]}..."}}')
print()
print("Example endpoint: STK push (prompt customer to pay)")
print("  POST" \
"https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest")

# The M-Pesa Daraja sandbox is free to test. When you build your quotation generator 
# or appointment bot in Phase 2, connecting M-Pesa payments uses exactly this flow. 
# Save your Consumer Key and Secret in a .env file, never in your code.