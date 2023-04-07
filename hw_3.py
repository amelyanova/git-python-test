#3.1Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# new_list = [ i for i in list_1 if isinstance(i, int)]
# print(sum(new_list))
#
# new_list_2 = [ i for i in list_1 if isinstance(i, str) and "a" in i ]
# print(new_list_2)

# # 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# animals = ['cat', 'dog', 'horse', 'cow' ]
# print(tuple(animals))
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
# 1) Программа имеет два input() - например, family_1, family_2.
# 2) Членов семьи нужно перечислить через запятую.
# Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
#
# family_1 = input("Состав семьи_1: ")
# family_2 = input("Состав семьи_2: ")
# family_list_1 = family_1.split(',')
# family_list_2 = family_2.split(',')
# print(family_list_1)
# print(family_list_2)
# if len(family_list_1) > len(family_list_2):
#     print(family_list_1)
# elif len(family_list_2) > len(family_list_1):
#     print(family_list_2)
# else:
#     print("Equal")

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# film = {"title":"Plut in city", "director": "Angelina", "year":2023, "budget": 1000, "main_actor": "Oleg", "slogan": 'Mew'}
# print(film.items())
# print(film.keys())
# print(film.values())


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list_1))


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# - найдите значения, которые встречаются в обоих множествах
# - найдите значения, которые не встречаются в обоих множествах
# - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))