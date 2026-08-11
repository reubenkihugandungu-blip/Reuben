# Lists are not fixed.
#  You can replace any item by assigning a new value to its index position.

fasting_protocols = ["OMAD", "2MAD", "16:8", "Autophagy marathon"]
print("Before:", fasting_protocols)

# Update the third item (index 2)
fasting_protocols[2] = "Extended 72hr"
print("After:", fasting_protocols)
# Listing every fasting mode in fasting protocols.
for fasting in fasting_protocols:
    print("Fasting:", fasting)