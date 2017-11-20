from math import atan, log

print("Formula 1: G = 4 * (-4 * a ** 2 + a * x + 5 * x ** 2) / -20 * a ** 2 + 28 * a * x + 3 * x ** 2")
print("Formula 2: F = atan(24 * a ** 2 - 25 * a * x + 6 * x ** 2)")
print("Formula 3: Y = log(2 * a ** 2 - 7 * a * x + 6 * x ** 2 + 1)")
choice = int(input("Select what tou want:"))

if choice == 1:
    x = float(input("Enter x:"))
    a = float(input("Enter a:"))
    denominator = -20 * a ** 2 + 28 * a * x + 3 * x ** 2
    if denominator == 0:
        print("The input values do not belong to the domain of the function definition")
        exit()
    G = 4 * (-4 * a ** 2 + a * x + 5 * x ** 2) / denominator
    print("G =", G)
elif choice == 2:
    x = float(input("Enter x:"))
    a = float(input("Enter a:"))
    F = atan(24 * a ** 2 - 25 * a * x + 6 * x ** 2)
    print("F =", F)
elif choice == 3:
    x = float(input("Enter x:"))
    a = float(input("Enter a:"))
    if x < 0 or a < 0:
        print("The input values do not belong to the domain of the function definition")
        exit()
    Y = log(2 * a ** 2 - 7 * a * x + 6 * x ** 2 + 1)
    print("Y =", Y)
else:
    print("Error")
    exit()
