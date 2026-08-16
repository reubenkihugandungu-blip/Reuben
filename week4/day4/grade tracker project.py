# This is your Week 4 project.
#  You will build a grade tracker that reads student data from a simulated CSV, processes it with functions,
#  handles bad data using error handling, computes averages and letter grades, then outputs a clean report. 
# Every skill from this week appears in this project.

# name,score1,score2,score3
#James Omondi,85,90,78
#Sandra Weru,72,,88
#Patrick Njiru,91,87,94
#Grace Achieng,60,bad data,70
#Brian Kamau,55,48,62

# Preview the data
import csv, io

csv_data = """name,score1,score2,score3
James Omondi,85,90,78
Sandra Weru,72,,88
Patrick Njiru,91,87,94
Grace Achieng,60,bad data,70
Brian Kamau,55,48,62"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
  print(dict(row))

# Parse Scores safely- write a function that tries to convert a score to an integer. if it fails return None

def parse_score(value):
  try:
    return int(value)
  except (ValueError, TypeError):
    return None
# Test
print(parse_score("85"))
print(parse_score(""))
print(parse_score("bad data"))
print(parse_score(None))

# Calculate Average and Letter Grade
# Write a function to calculate the average of valid scores only and another to assign a letter grade

def calculate_average(scores):
  valid = [s for s in scores if s is not None]
  if not valid:
    return None
  return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
  if avg is None:
    return "N/A"
  if avg >= 90:
    return "A"
  elif avg >= 80:
    return "B"
  elif avg >= 70:
    return "C"
  elif avg >= 60:
    return "D"
  else:
    return "F"
# Test
scores_a = [85, 90, 78]
scores_b = [72, None, 88]
scores_c = [60, None, None]

for s in [scores_a, scores_b, scores_c]:
  avg = calculate_average(s)
  print(f"Scores: {s} | Avg: {avg} | Grade: {letter_grade(avg)}")
# 