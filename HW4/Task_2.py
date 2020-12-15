import random

numbers = random.sample(range(0,100), 10)
from_int_to_float = [float(item) for item in numbers]


print(from_int_to_float)
item_num = 0
while item_num < len(numbers):
    numbers[item_num] = float(numbers[item_num])
    item_num += 1
print(numbers)