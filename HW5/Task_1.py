range_list = range(1, 11)
even = [number for number in range_list if number%2 == 0]
odd_divisible_by_3 = [number for number in range_list if number%2 == 1 and number%3 == 0]
not_divisible_by_2_and_3 = [number for number in range_list if number%2 != 0 and number%3 !=0]
print(f"even: {even}")
print(f"odd numbers, which are divisible by 3: {odd_divisible_by_3}")
print(f"numbers that are not divisible by 2 and 3: {not_divisible_by_2_and_3}")