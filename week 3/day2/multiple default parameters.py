def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps} | Water: {water} | Protocol: {protocol}")

log_day(9200) # uses both default values for water and protocol
log_day(10500, water=9) # overrides the default value for water, but uses the default for protocol
log_day(8800, water=7, protocol="2MAD") # overrides both default values for water and protocol