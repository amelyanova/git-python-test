# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помо
# щью кортежа):периметр квадрата, площадь квадрата и диагональ квадрата.
# from math import sqrt
from functools import reduce

from calc import summa, division, multiplay, subtraction

# def square(x):
#     P = 4*x
#     S = x**2
#     D = sqrt(2 * S)
#     return (P, S, D)
# print(square(5))


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# в формате аргумент: значение. Например:
# name: John
# last_name: Smith
# age: 35
# position: web developer

# def user(**kwargs):
#     for z,o in kwargs.items():
#         print(z,o)
#
# user(name="John", last_name="Smith",position="web developer", age=35)






# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# filtered_list = list(filter(lambda x: x>0,my_list))
# print(filtered_list)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# my_list = [20, -3, 15, 2, -1, -21]
# new_list = reduce(lambda x,y: x*y, my_list)
# print(new_list)

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

# NO please

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.


# print(summa(2,5))
# print(division(10,2))
# print(multiplay(10,2))
# print(subtraction(10,2))
