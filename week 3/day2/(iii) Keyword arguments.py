# When calling a function, you can pass arguments by name instead of position. 
# This is called a keyword argument.
#  It makes the call easier to read and lets you skip over some parameters.

def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"{name} | Goal: {goal} | Sessions/week: {sessions} | Bench Press: {bench_kg}kg")

# positional arguments
client_report("James", "fat loss")

# keyword arguments: order of arguments doesn't matter
client_report(goal="muscle gain", name="Mwangi", bench_kg=100,)

# Mixing positional and keyword arguments: positional arguments must come first
client_report("Sandra", "endurance", bench_kg=50) # positional arguments first