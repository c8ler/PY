a = input('введите числа через пробел: ')

def num (a):
    f = [int(s) for s in a.split()]
    print(f)
    print(f"min {min(f)}, max {max(f)}")

num(a)