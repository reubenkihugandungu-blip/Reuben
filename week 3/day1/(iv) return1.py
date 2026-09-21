# Write a function called get_status(steps) that returns
#  "Exceeded", "Hit", or "Missed" depending on whether steps is above 10000, between 8000 and 10000, 
# or below 8000. 
# Then call it and print the result.


def get_status(steps):
    if steps > 10000:
        return "Exceeded"
    elif steps >= 8000:
        return "Hit"
    else:
        return "Missed"
# Call the function and print the result
print(get_status(12000))  # Exceeded
print(get_status(9000))   # Hit
print(get_status(7000))   # Missed