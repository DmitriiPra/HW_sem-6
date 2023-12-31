"""
Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""


def find_range_index(arr, low, up):
    index_list = []
    for i in range(len(arr)):
        if low <= arr[i] <= up:
            index_list.append(i)
    return index_list


spisok = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
lower = int(input("Введите нижнее значение диапазона: "))
upper = int(input("Введите верхнее значение диапазона: "))

print(find_range_index(spisok, lower, upper))
