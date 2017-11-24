from math import atan, log
choice = 1
results = []
counter = 0
results_str = ""
index = 0
while choice != 0:

    print("1: G = 4 * (-4 * a ** 2 + a * x + 5 * x ** 2) / -20 * a ** 2 + 28 * a * x + 3 * x ** 2")
    print("2: F = atan(24 * a ** 2 - 25 * a * x + 6 * x ** 2)")
    print("3: Y = log(2 * a ** 2 - 7 * a * x + 6 * x ** 2 + 1)")
    print("4: - Program for finding even numerals in the number")
    print("Select 0 to quit")
    choice = int(input("Select what tou want:"))
    while choice > 4 or choice < 0:
        print("Invalid value, try again")
        choice = int(input("Select what tou want:"))
    if choice == 0:
        print("Shutdown...")
        break

    x_min = str(input("Enter minimum value of x:"))
    x_min = float(x_min)
    x_max = str(input("Enter maximum value of x:"))
    x_max = float(x_max)
    while x_min > x_max:
        print("Maximum value of x should be grater than the minimum")
        x_max = float(input("Enter maximum value of x again:"))

    a = float(input("Enter a:"))

    steps = str(input("Enter the number of steps:"))
    steps = int(steps)
    while steps <= 0:
        print("Error,the number of steps can not be less than or equal to 0")
        steps = int(input("Enter the number of steps again:"))

    x = x_min

    if choice == 1:
        for i in range(steps):
            ind = 0
            denominator = -20 * a ** 2 + 28 * a * x + 3 * x ** 2
            if denominator == 0:
                print("The input values do not belong to the domain of the function definition")
                break
            G = 4 * (-4 * a ** 2 + a * x + 5 * x ** 2) / denominator
            results.append(G)
            print("x =", x, "\tG =", G)
            x += (x_max - x_min) / (steps - 1)
            results_str += str(G)
    elif choice == 2:
        for i in range(steps):
            F = atan(24 * a ** 2 - 25 * a * x + 6 * x ** 2)
            results.append(F)
            print("x =", x, "\tG =", F)
            x += (x_max - x_min) / (steps - 1)
    elif choice == 3:
        for i in range(steps):
            if x < 0 or a < 0:
                print("The input values do not belong to the domain of the function definition")
                break
            Y = log(2 * a ** 2 - 7 * a * x + 6 * x ** 2 + 1)
            results.append(Y)
            print("x =", x, "\tG =", Y)
            x += (x_max - x_min) / (steps - 1)

    print("Minimum value =", min(results))
    print("Maximum value =", max(results))
    print(str(results_str))

    template = str(input("Enter template:"))
    print(results_str.count(template))

    list.clear(results)
