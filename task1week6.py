import math
import statistics

numbers = [25, 36, 49, 64, 81]

square_roots = [math.sqrt(num) for num in numbers]
print("Square roots:", square_roots)

average = statistics.mean(numbers)
print("Average:", average)
