a = int(input("Введите число -> "))

x = []
integer = []
result = []

x = list(str(a))[::-1]


while True:
    if a != 0:
        if a % 2 == 0:
            result.append(0)
            a = a // 2
        elif a % 2:
            result.append(1)
            a = a // 2
    else:
        result.reverse()
        print(result)
        break