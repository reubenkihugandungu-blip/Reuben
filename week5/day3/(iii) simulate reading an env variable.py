import os

# Simulate: key loaded from environment (not hard coded)
os.environ["SMP_API_KEY"] = "smp_test_key_abc123" # set for demo only

api_key = os.environ.get("SMP_API_KEY")

if not api_key:
    print("Error: API key not found. Set the SMP_API_KEY environment variable.")
else: 
    # Show only first 8 chars for safety
    masked = api_key[:8] + "..." + api_key[-4:]
    print(f"Key loaded: {masked}")
    print("Ready to make authenticated requests.")