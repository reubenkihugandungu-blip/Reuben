# Takes a list of daily fasting protocols and returns a count of how many days used each protocol.

def protocol_summary(protocol_list):
    unique = list(set(protocol_list))# converts protocol list to a set to remove duplicates then back to a list called unique
    summary = {} # creates an empty dictionary to store counts per protocol
    for p in unique: # loops over each unique protocol
        summary[p] = protocol_list.count(p) # counts how many times p appears in protocol list and stores that count under key p in summary
    return summary # returns the summary dictionary mapping protocol count

protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
result = protocol_summary(protocols) # calls protocol summary with protocols and stores the returned dictionary in result

print("Protocol breakdown:")
for protocol, days in result.items():# iterates over key/value pairs in result
    print(f" {protocol}: {days} day(s)")