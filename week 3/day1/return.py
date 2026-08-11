# return exits the function and sends a value back to the caller. 
# You can store that value in a variable, use it in a calculation, or pass it to another function.

def calculate_average_steps(steps_list):
    total_steps = sum(steps_list)
    average_steps = total_steps // len(steps_list)
    return average_steps

week_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
avg = calculate_average_steps(week_steps)
print("Average steps for the week:", avg)
#

    