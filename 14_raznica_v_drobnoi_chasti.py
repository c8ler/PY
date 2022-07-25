a = [1.1, 1.2, 3.1, 5.10, 10.01]
def MaxMin(list):
    for i in range(len(list)):
        list[i]=(list[i]%1)
    Result=round(max(list),3)-round(min(list),3)
    return f'Разница между остатком дробей {round(max(list),3)} и {round(min(list),3)} = {Result}'
print(MaxMin(a))