from datetime import date

# How many days until a goal date?
today = date.today() # calls date.today to get the current date and stores it in the variable today
goal_date = date(2026, 12, 31) # creates a date for Dec 31 2026 & store it as goal_date
days_left = (goal_date-today).days # subtracts today from goal_date. producing a timedelta, then accesses days to get the number of days between them.

print(f"Days until end of 2026: {days_left}")

# Format date as  text
formatted = today.strftime("%d %B %Y") # formats today into a string using strftime
print("Today's date:", formatted)