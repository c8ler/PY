def Calc(arg1, arg2, oper):
    if oper == '+':
        return arg1 + arg2
    if oper == '-':
        return arg1 - arg2
    if oper == '*':
        return arg1 * arg2
    if oper == '/':
        return arg1 / arg2


status = True
while status != False:
    arg_one = float(input("введите число 1 "))
    operation = input("введите операцию ")
    arg_two = float(input("введите число 2 "))

    result = Calc(arg_one, arg_two, operation)
    print(round(result))

    status = input('Введите "q", чтобы выйти из программы.')
    if status == 'q' or status == 'quit':
        status = False