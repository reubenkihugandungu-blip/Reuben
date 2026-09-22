# else runs only when no exception occurred. 
# finally runs always, whether an exception occurred or not.
#  Use finally for cleanup actions like closing a file or connection.

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("(Calculation attempted)")
    print()

safe_divide(100, 4)
safe_divide(100, 0)
safe_divide(9200, 7)

