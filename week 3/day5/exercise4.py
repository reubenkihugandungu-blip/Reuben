# Write a function that takes a list of scores
# and returns the average, highest, and lowest

def analyse(scores):
    return {
         "average": sum(scores) / len(scores),
         "highest": max(scores),
         "lowest": min(scores) 
    }

result = analyse([78, 91, 63, 85, 72])
for k, v in result.items():
    print(f"{k}: {v}")