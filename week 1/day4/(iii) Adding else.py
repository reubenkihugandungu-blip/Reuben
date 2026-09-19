# else is the "if not" part. It runs when the if condition is false.
# Between if and else exactly one of them will always run.

# IF + ELSE: CHECK

steps = 9000

if steps >= 8000:
    print("Target hit. Well done.")
else:
    print(f"Target missed. You need {8000 - steps} more steps.")

# Try changing the number to 9000 and run again