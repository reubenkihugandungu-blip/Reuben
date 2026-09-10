# Tell the model to respond in JSON. 
# Parse the response with json.loads() to get a Python dictionary. This lets you use AI output programmatically.

# EXTRACT STRUCTURED OUTPUT
import json

# System prompt requesting JSON output
system = """You are a fitness data extractor.
Parse the user's daily log and return ONLY valid JSON with these keys:
steps (int), sleep_hours (float), protocol (str), cold_shower (bool), water_glasses (int).
No other text."""

# What the AI would return for this input
raw_log = "Today I did 9,200 steps, slept for 7.5 hours, followed OMAD, took a cold shower and drank 8 glasses of water."

# Simulated AI JSON response
simulated_json_response = '{"steps": 9200, "sleep_hours": 7.5, "protocol": "OMAD", "cold_shower": true, "water_glasses": 8}'

# Parse it
try:
    parsed = json.loads(simulated_json_response)
    print("Parsed structured data:")
    for key, value in parsed.items():
        print(f"  {key}: {value}")

    # Use it programmatically
    print()
    if parsed["steps"] >= 10000:
        print("Step goal: HIT")
    else:
        print(f"Step goal: {parsed['steps']:,}/10,000 ({10000 - parsed['steps']:,} short)")
    print(f"Sleep rating: {'Good' if parsed['sleep_hours'] >= 7.5 else 'Low'}")

except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")

# Try this:
# Change the raw_log string in the last terminal to your own daily description. 
# The simulated parser extracts the same values. In VS Code with a live key, 
# the actual AI would parse any natural language you give it.