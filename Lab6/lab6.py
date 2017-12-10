from math import atan, log
choice = 1
results = []
qwe = {}
counter = 0
Final_result = ""
G_result = ""
F_result = ""
Y_result = ""
G_results = []
F_results = []
Y_results = []
Final_results = []
index = 0
i = 0

while choice != 0:

    print("Enter 1 to start the program")
    print("Enter 0 to quit")
    choice = int(input("Select what tou want:"))
    while choice < 0 or choice > 1:
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

    while x <= x_max:
        denominator = -20 * a ** 2 + 28 * a * x + 3 * x ** 2
        if denominator == 0:
            print("The input values do not belong to the domain of the function definition")
            break
        G = 4 * (-4 * a ** 2 + a * x + 5 * x ** 2) / denominator
        result = {'G': G}
        results.append(result)
        print("x =", x, "\tG =", results[i]['G'])
        G_results.append(G)
        Final_results.append(G)
        x += (x_max - x_min) / (steps - 1)
        G_result += str(G)
        i += 1

    print("\nMinimum value =", min(G_results))
    print("Maximum value =", max(G_results))
    print("Result string -", str(G_result))

    template = str(input("Enter template:"))
    print("Number of coincidences:", G_result.count(template))

    Final_result += G_result

    print("\n**********************************\n")

    x = x_min

    while x <= x_max:
        F = atan(24 * a ** 2 - 25 * a * x + 6 * x ** 2)
        result = {'F': F}
        results.append(result)
        print("x =", x, "\tF =", results[i]['F'])
        F_results.append(G)
        Final_results.append(F)
        x += (x_max - x_min) / (steps - 1)
        F_result += str(F)
        i += 1

    print("\nMinimum value =", min(F_results))
    print("Maximum value =", max(F_results))
    print("Result string -", str(F_result))

    template = str(input("Enter template:"))
    print("Number of coincidences:", F_result.count(template))

    Final_result += F_result

    print("\n**********************************\n")

    x = x_min

    while x <= x_max:
        if x < 0 or a < 0:
            print("The input values do not belong to the domain of the function definition")
            break
        Y = log(2 * a ** 2 - 7 * a * x + 6 * x ** 2 + 1)
        result = {'Y': Y}
        results.append(result)
        print("x =", x, "\tY =", results[i]['Y'])
        Y_results.append(G)
        Final_results.append(Y)
        x += (x_max - x_min) / (steps - 1)
        Y_result += str(Y)
        i += 1

    print("\nMinimum value =", min(Y_results))  
    print("Maximum value =", max(Y_results))
    print("Result string -", str(Y_result))

    template = str(input("Enter template:"))
    print("Number of coincidences:", Y_result.count(template))

    Final_result += G_result

    print("\nFinal minimum value =", min(Final_results))
    print("Final maximum value =", max(Final_results))
    print("Final result string -", Final_result,)

    template = str(input("Enter template:"))
    print("Number of coincidences:", Final_result.count(template), "\n")
