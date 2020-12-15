even_numbers_via_for = []
even_number_via_while = []

for number in range(100):
    if number%2 == 0 and number > 0:
        even_numbers_via_for.append(number)
print(even_numbers_via_for)

number = 0
while number < 100:
    if number % 2 == 0 and number > 0:
        even_number_via_while.append(number)
    number += 1
print(even_number_via_while)