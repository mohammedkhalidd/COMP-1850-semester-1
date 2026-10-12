# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error no numbers provided")
minimum = min(numbers)
maxmimun = max (numbers)
mean = sum(numbers) / len(numbers)
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
print(f"Minimum = {minimum}")
print(f"Maximum = {maxmimun}")
print(f"Mean = {mean}")
print(f"Median {median}")