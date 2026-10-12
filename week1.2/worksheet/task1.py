# Worksheet 1.2: Task 1 Solution
import sys
grade_input = input("Enter an integer grade (0-100):")
if not grade_input.isdigit():
   sys.exit("Error: Grade must be a integer between (0-100):")
grade = int(grade_input)
if grade <0 or grade > 100:
  sys.exit("Error: Grade must be a integer between (0-100):")
if 0 <= grade <= 39:
   result = "Fail"
elif 40 <= grade <= 69:
   result = "Pass"
else:
   result = "Distinction"
print(f"{grade} is a {result}") 