# You can have multiple parameters. 
# Separate them with commas in both the definition and the call.

def log_day(day, steps, protocol):
    print(f"{day}: {steps} steps | protocol: {protocol}")

log_day("Monday", 9200, "OMAD")
log_day("Tuesday", 10500, "OMAD")
log_day("Wednesday", 8800, "Autophagy Marathon")
log_day("Thursday", 10500, "2MAD")
