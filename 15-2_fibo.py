def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)

    for i in range(2, n+1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n-2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    return fibo_list

x = fibo(10)
print(x)