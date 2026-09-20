# sort() rearranges a list in ascending order (lowest to highest for numbers, A to Z for text).
#  It changes the list directly.

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print("Unsorted:", weekly_steps)

weekly_steps.sort()
print("Sorted low to high:", weekly_steps)

weekly_steps.sort(reverse=True) # sort high to low by passing reverse=True
print("Sorted high to low:", weekly_steps)

print()

# reverse() flips the order of the list without sorting it. It just turns the list backwards.

skills = ["welding", "tiling", "upholstery", "phone repair"]
skills.reverse()
print(skills)

print()

# count() counts how many times a specific value appears in the list.

daily_results = ["hit", "miss", "hit", "hit", "miss", "hit", "hit"]
hit_count = daily_results.count("hit")
miss_count = daily_results.count("miss")
print("Days goal hit:", hit_count)
print("Days missed:", miss_count)

