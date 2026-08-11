# // integer division divides and drops the decimal.
# modulo %  returns what is left after dividing.

total_steps = 65000
days = 7

# clean whole number average (no decimal)
daily_average = total_steps // days
print(f"Daily average: {daily_average} steps")

# How many full sets of 1000 steps?
full_thousands = total_steps // 1000
print(f"Full thousands: {full_thousands}")

# Power: how many steps in 2 weeks squared?
print(f"8000 to the power of 2: {8000 ** 2}")
