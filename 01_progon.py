def progon(num):
    for i in range(-num, num + 1, 1):
        print(i, end = ' ')

number = input('Введите число: ')
try:
    number = int(number)
    progon(number)
except:
    print('Введите целое число')
