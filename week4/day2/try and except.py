# Wrap code that might fail in a try block. Put your response in the except block. 
# If the try block fails, Python jumps to except instead of crashing.

steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, "- Goal hit")
        else:
            print(steps, "- Below goal")
    except ValueError:
        print(f"'{item}'' is not a valid number. Skipping.")


