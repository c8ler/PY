from math import sqrt


A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

D = B**2 - 4*A*C

if D == 0:
    x = -B/(2*A)
    print(f"Уравнение имеет один корень: {x}")
elif D > 0:
    x1 = (-B + sqrt(D)) / (2 * A)
    x2 = (-B - sqrt(D)) / (2 * A)
    print(f"Уравнение имеет два корня: x1={round(x1, 3)}; x2={round(x2, 3)}")
else:
    print("Уравнение не имеет вещественных корней")