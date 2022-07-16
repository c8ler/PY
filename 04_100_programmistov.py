def abv(num):
    if (num == 1) or (num > 20 and num % 10 == 1) or (num > 99 and num % 100 == 1):
        print(f'{num} программист')
    elif (2 <= num <= 4) or (num > 20 and 2 <= num % 10 <= 4) or (num > 99 and 2 <= num % 100 <= 4):
        print(f'{num} программиста')
    else:
        print(f'{num} программистов')


for i in range(0, 51, 1):
    abv(i)