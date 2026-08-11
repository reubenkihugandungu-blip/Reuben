# datetime works with dates and times. 
# You can get today's date, format it as text, and calculate the number of days between two dates.

from datetime import datetime, date

# Today's date and time
now = datetime.now()
print("Current datetime:", now)

# Just the date
today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Days between two dates
start = date(2025, 1, 1)
end = date(2025, 12, 31)
delta = end - start
print("Days in 2025:", delta.days)

