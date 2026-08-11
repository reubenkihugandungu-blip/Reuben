# and means both conditions must be true, for the whole thing to be true.
#  or means atleast one must be true.

steps = 7900
water_glasses = 8
cold_shower = True
sleep_hours = 7

if steps >= 8000 and water_glasses >= 8:
    print("Steps and water: both on target.")
else:
    print("Steps or water below target.")

if sleep_hours >= 7 and cold_shower:
    print("Sleep and cold shower: both done.")
else:
    print("Sleep or cold shower missed.")
