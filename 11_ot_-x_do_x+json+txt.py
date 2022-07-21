import json

a = int(input('введите число -> '))

def numprint(x):
    x = list(range(-x, x+1))
    return x

b = numprint(a)
print(b)
with open('data.json', 'a', encoding='utf-8') as fh:
    fh.write(json.dumps(b, ensure_ascii=False))
# загружаем из файла данные в словарь data
print('Данные формата Json успешно сохранены')
#print(type(BD)) # type(x) - формат файла

with open('data.txt', 'a') as fh:
    fh.write(str(b))
print("Данные сохранены в txt")