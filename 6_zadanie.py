# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# quantity = int(input('Введите количество элементов: '))
# numb = [0]*quantity
# numb[0] = int(input('Введиете первый элемент массива: '))
# difference = int(input('Введите разность элементов: '))
# print(numb[0],end=' ')
# for i in range(1,quantity):
#     numb[i]= numb[i-1]+difference
#     print(numb[i],end=' ')


# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
count = int(input("Колличество элементов: "))
lst_1 = [random.randint(0, 20) for i in range(count)]
print(lst_1)
lst_2 = []
max_1 = int(input("Введите максимум: "))
min_1 = int(input("Введите минимум: "))
# for i in range(len(lst_1)):
#     if lst_1[i] >= min_1 and lst_1[i] <= max_1:
#         lst_2.append(i)
# print(lst_2)
# или
for i in range(len(lst_1)):
    if min_1 <= lst_1[i] <= max_1:
        print(i, end=' ')