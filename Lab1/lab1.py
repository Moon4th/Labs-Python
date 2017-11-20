from math import atan, log

x = float(input("Enter x:"))
a = float(input("Enter a:"))
G = 4 * (-4 * a ** 2 + a * x + 5 * x ** 2) / (-20 * a ** 2 + 28 * a * x + 3 * x ** 2)
print("G =", G)

x = float(input("Enter x:"))
a = float(input("Enter a:"))
F = atan(24 * a ** 2 - 25 * a * x + 6 * x ** 2)
print("F =", F)

x = float(input("Enter x:"))
a = float(input("Enter a:"))
Y = log(2 * a ** 2 - 7 * a * x + 6 * x ** 2 + 1)
print("Y =", Y)
