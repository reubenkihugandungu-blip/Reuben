# sort() rearranges a list in ascending order (lowest to highest for numbers, A to Z for text).
#  It changes the list directly.

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print("Unsorted:", weekly_steps)

weekly_steps.sort()
print("Sorted low to high:", weekly_steps)

weekly_steps.sort(reverse=True) # sort high to low by passing reverse=True
print("Sorted high to low:", weekly_steps)
