while True:
    number = int(input("Enter number to find it's factorial: "))
    if number < 0:
        print("factorial of negative number doesn't exist ^^")     
        continue
    break
if number == 0:
    print("1")
factorial = 1
for i in range(factorial, number + 1):
    factorial *= i
print(f"factorial of {number} is {factorial}")