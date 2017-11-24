counter = 0
number = (input("Enter the number:"))
number = int(number)
while number != 0:
    if number % 2 == 0:
        counter += 1
        number = number // 10
    else:
        number = number // 10

print("Amount of even numbers:", counter)
