# # Wrap a division operation in try/except
# Handle ZeroDivisionError and ValueError separately

def safe_divide(a, b):# defines a function named safe_divide that takes two parameters a the dividend and b the divisor
    try:
        return a / b # attempts to divide  a by b and return the resultif b is 0 this will raise a zerodivision error
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError as e: # catches valuerror errors though unlikely in this code and stores the error details in variable e
        return f"Invalid input: {e}"

# print (safe_divide(10, 2)) # calls the function with 10 / 2 prints results 5.0
print (safe_divide(10, 0))# calls the function with 10/0 catches the error prints: cannot divide by zero