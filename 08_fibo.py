import time

def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input('Введите число элементов: '))

def fiboprint(x):
    for i in range(1, x+1):
        start = time.process_time()
        fibo(i)
        finish = time.process_time()
        print(f"{i}-й элемент вычисляется {finish - start:.3f} секунд")
    return list

fiboprint(x)