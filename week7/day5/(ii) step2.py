# Build the Coaching Layer

# The coaching layer receives the prediction result and the input values, then returns a structured coaching message.
#  In production this calls the OpenAI Chat API.
#  In this browser terminal it uses the same response structure with simulated output.

# Concept
# The coaching layer is a function that takes structured data in and returns a formatted coaching response out.
# It does not make decisions about whether to run or when. It only knows how to turn data into a message.

import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    prompt = (f"Athlete data: sleep {sleep}h, water {water} glasses, "
              f"bench {bench}kg. "
              f"Goal prediction: {'HIT' if hit_goal else 'MISS'} ({confidence:.0%} confidence). "
              "Give a 2-sentence coaching response. Be direct and specific.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": ("You are an SMP performance coach. "
                          "You give direct, data-driven coaching feedback. "
                          "No filler. Two sentences maximum.")},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Coaching layer
# Simulated coaching layer
# The response structure mirrors the OpenAI API object

class SimulatedMessage:
    def __init__(self, content):
        self.content = content

class SimulatedChoice:
    def __init__(self, content):
        self.message = SimulatedMessage(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [SimulatedChoice(content)]

COACHING_TEMPLATES = {
    # key: (hit_goal, sleep_ok, water_ok)
    (True, True, True):  ("Strong inputs, strong output. Sleep and hydration are locked in.",
                          "Keep this baseline consistent and the steps will follow."),
    (True, True, False): ("You hit the goal despite low water. Sleep is your biggest lever.",
                          "Push hydration tomorrow and the margin grows."),
    (True, False, True): ("Water carried today's performance despite low sleep.",
                          "Shore up sleep tonight. Hitting goals on low sleep has hidden costs."),
    (True, False, False): ("Goal hit through willpower, not system. Willpower runs out.",
                           "Fix sleep and water before the next session."),
    (False, True, True): ("Inputs were solid but the goal was missed.",
                          "Audit what absorbed the energy. Do not cut sleep or water."),
    (False, True, False): ("Sleep is solid, hydration is low, goal was missed.",
                           "Add two glasses of water tomorrow. Hydration shifts step counts more than expected."),
    (False, False, True): ("Low sleep is the lead variable. Water is fine.",
                           "Get to bed 45 minutes earlier. The effect shows within 72 hours."),
    (False, False, False): ("Both inputs are below threshold and the goal was missed.",
                            "Reset tonight: 8 hours sleep minimum, 10 glasses water tomorrow."),
}

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    """Simulated coaching. Real version calls OpenAI Chat API."""
    sleep_ok = sleep >= 7.0
    water_ok = water >= 8
    key = (bool(hit_goal), sleep_ok, water_ok)
    line1, line2 = COACHING_TEMPLATES[key]
    coaching_text = f"{line1} {line2}"
    return SimulatedResponse(coaching_text)

# Test the coaching layer directly
test_cases = [
    (8.0, 10, 90, True,  0.91),
    (5.5, 4,  70, False, 0.88),
    (7.5, 6,  85, True,  0.74),
]

for sleep, water, bench, hit, conf in test_cases:
    response = get_coaching_message(sleep, water, bench, hit, conf)
    message = response.choices[0].message.content
    outcome = "HIT GOAL" if hit else "MISS GOAL"
    print(f"[{outcome} | {conf:.0%} confidence]")
    print(f"Sleep: {sleep}h | Water: {water} glasses | Bench: {bench}kg")
    print(f"Coach: {message}")
    print("-" * 60)

# Tip:
#  The coaching templates use a tuple key (hit_goal, sleep_ok, water_ok).
#  This covers all 8 combinations without nested if-statements.
#  In production you replace the dict lookup with a live API call and the logic lives in the system prompt instead.


