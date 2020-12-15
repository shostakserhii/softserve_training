even_numbers_via_continue = []

for number in range(100):
    if number % 2 == 0:
        continue
    even_numbers_via_continue.append(number)
print(even_numbers_via_continue)