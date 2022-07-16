def funk(count):
    a = count % 10
    if (count == 11 or count == 12 or count == 13 or count == 14):
        return 'программистов'
    elif (a == 0):
        return 'программистов'
    elif (a == 1):
        return 'программист'
    elif (2 <= a) and (a <= 4):
        return 'программиста'
    else:
        return 'программистов'


for i in range(0, 51, 1):
    print(f'{i} {funk(i)}') 