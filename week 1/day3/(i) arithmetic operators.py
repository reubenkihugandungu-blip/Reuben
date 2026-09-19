# An operator is a symbol that performs an action. + adds. - subtracts. * multiplies. / divides. 
# Python evaluates the expression and gives you the result.

# ARITHMETIC OPERATORS 

morning_steps = 4200
afternoon_steps = 5000

#Addition
total_steps = morning_steps + afternoon_steps
print(f"Total steps:{total_steps}")

#Subtraction
steps_remaining = 10000 - total_steps
print(f"steps to reach 10,000: {steps_remaining}")

#Multiplication
weekly_target = 8000 * 7
print(f"weekly step target: {weekly_target}")

#Division
daily_average = 65000 / 7 # use integer division // for to get a whole number
print(f"Daily average this week: {daily_average}")

# Notice that division always returns a decimal, even when the answer is a whole number.
#  65000 / 7 gives you 9285.714....If you want only the whole number part, use integer division.