# ValueError	Wrong type of value (e.g. converting "abc" to int)
#ZeroDivisionError - Dividing a number by zero
#KeyError - Accessing a dictionary key that does not exist
#IndexError	- Accessing a list index that does not exist
#TypeError	- Wrong type used in an operation
# Different errors need different responses. You can have multiple except blocks to handle each type.

# Multiple except blocks
def calculate_average(steps_list): # defines a function named calculate_average, accepts one parameter steps_list which should be a list of step counts.
    try: # starts a try block to run code that may raise excemptions, if an error occurs inside this block, execution jumps to a matching except.
        total = sum(steps_list) # calculate the sum of all items in the steps_list
        avg = total / len(steps_list)
        return round(avg) # rounds the average to the nearest integer and returns it, if no exception happened the function ends here.
    except ZeroDivisionError:# handles the case where the list is empty and division by zero occured this prevents the program from crashing.
        print("Error: List is epmty. Cannot calculate average.")
        return 0 # returns 0 as a fallback value when the average cannot be computed.
    except TypeError:
        print("Error: List contains non-numeric values.")
        return 0 # Returns 0 again as a safe fallback

print("Average:", calculate_average([9200, 10500, 8800, 11000]))# calls the function with valid numeric data & prints the average of the list
print("Average:", calculate_average([]))# zerodivisonerror
print("Average:", calculate_average([9200, "eight thousand", 10500]))#typeError