"""
Задание 30
Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для 
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15

"""


def arithmetic_progression(a: int, n: int, b: int) -> list:
    if b <= 0:
        return ["введено некоректное значение количества элементов прогрессии"]

    return [(a + (i - 1) * n) for i in range(b)]




start_number = int(input("введите число a: "))
difference = int(input("введите значение разности: "))
quantity = int(input("введите количество элементов: "))

print(start_number, difference, quantity)
print(*arithmetic_progression(start_number, difference, quantity))
