input1 = [2, 3, 4, 5, 6]
input2 = [2, 3, 5, 6]


def fun(lst):
    result = []
    for i in range(0, len(lst)//2 if len(lst) % 2 == 0 else len(lst)//2 + 1):
        result.append(lst[i] * lst[-i-1])
    return result


print(fun(input1))
print(fun(input2))