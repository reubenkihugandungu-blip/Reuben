# Takes a list of daily step counts and an optional goal (default 8,000). Returns a summary of the week.
# defining a function named weekly steps summary that takes steps list and an optional goal parameter defaulting to zero

def weekly_step_summary(steps_list, goal=8000):
    days_hit = len([s for s in steps_list if s >= goal])# creates a list of step values that meet or exceed goal then counts how many such days there are.
    average = sum(steps_list) / len(steps_list)
    best = max(steps_list) # finds the highest step count in the list.
    worst = min(steps_list) # 

    return {          # starts returning a dictionary containing the summary values.
        "days_on_goal": days_hit, # adds the count of days that reached the goal
        "total_days": len(steps_list), # adds the total number of days in the input list.
        "average": round(average), # adds the average step count, rounded to the nearest whole number.
        "best_day": best, # adds the highest step count
        "worst_day": worst # adds the lowest step count.
    } # closes the dictionary returned by the function.

weekly = [9200, 7500, 10500, 8800, 6900, 11000, 9600] # defines a list of step counts for one week
result = weekly_step_summary(weekly) # calls the function with the weekly list and stores the returned summary in result

print("Step Summary:")
print(f" Days on goal : {result['days_on_goal']}/{result['total_days']}") # p the number of days that met the goal out of the total days.
print(f" Average : {result['average']} steps") # p the rounded average daily step count.
print(f" Best day : {result['best_day']} steps") # prints the highest step count recorded
print(f" Worst day : {result['worst_day']} steps")
