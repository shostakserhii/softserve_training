import random

random_list = []

for i in range(0,3):
    number = random.randint(1,10)
    random_list.append(number)
print(random_list)
for number in random_list:
    if number % 2 != 0:
        print("Odd number has been found!")
        break
    print("not found")