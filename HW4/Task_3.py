while True:
    value = input("Enter value till we gonna 'fibo' : ")
    if value.isdigit():
        break
    print("you gotta enter digit or force quit app!")
    continue
x = 0
y = 1
while y < int(value):
    x, y = y, x + y
    print(y)
print(x)