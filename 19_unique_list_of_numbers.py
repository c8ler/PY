# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
def UniqueNumbers(numbers):
    result=[i for i in numbers if numbers.count(i)==1]
    return result
print(UniqueNumbers(numbers))