#
# def pas():
#     list_pas = []
#     lock = 0
#     range_lock = range(3, 21)
#     number_lock = random.choice(range_lock)
#     lock += number_lock
#     range_pas = range(1, 21)
#     for i in range_pas:
#         range_pas_2 = range(i + 1, 21)
#         for j in range_pas_2:
#             if i != lock and j != lock and lock % (i + j) == 0:
#                 list_pas.append(i)
#                 list_pas.append(j)
#     print(f'{lock} - число из первой вставки')
#     print(list_pas, '- нужный пороль')
#
#
# pas()


# def send_email(message, recipient, sender="university.help@gmail.com"):
#     if ("@" not in recipient or not recipient.endswith((".com", ".ru", ".net"))
#             or "@" not in sender or not sender.endswith((".com", ".ru", ".net"))):
#         print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
#     elif sender == recipient:
#         print("Нельзя отправить письмо самому себе!")
#     elif sender == "university.help@gmail.com":
#         print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
#     else:
#         print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
#
# # Примеры вызова функции
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



# # Задача 2
# # Даны списки:
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result_1 = list(filter(lambda elem: elem in list_2, list_1))
# # Вывод
# print(result_1)
#
# result_2 = list(set(list_1) & set(list_2))
# # Вывод
# print(result_2)
#
#
# # Напишите программу для слияния нескольких словарей в один.
#
#
# result_3 = list_1 + list_2      # Оператор «+» можно использовать для объединения двух списков.
# result_3.sort()                 # Он добавляет один список в конец другого списка и дает новый список в качестве вывода.
# # Вывод
# print(result_3)
#
#
# for i in list_2:        # В методе Naive цикл for используется для обхода второго списка.
#     list_1.append(i)    # После этого элементы из второго списка добавляются к первому списку.
# # Вывод                 # Первый список является объединением первого и второго списков.
# print(str(a))
#
#
# result_4 = [j for i in [list_1, list_2] for j in i]     # Concatenated list в Python – это альтернативный метод объединения двух списков в Python.
# # Вывод                                                 # Понимание списка – это в основном процесс построения и генерации списка элементов на основе существующего списка.
# print(result_4)                                         # Он использует цикл for для обработки и обхода списка поэлементно.
#                                                         # Приведенный ниже встроенный цикл for эквивалентен вложенному циклу for.
#
# list_1.extend(list_2)   # Метод extend() можно использовать для объединения двух списков в Python.
# # Вывод                 # Все элементы 'list_2' добавляются к 'list_1', и, таким образом, "list_1" обновляется и выводится.
# print(list_1)



# Напишите программу для слияния нескольких словарей в один.

# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
#
# list = {}
# for i in (dict_a, dict_b, dict_c):
#     list.update(i)
#     print(list)
#
# print()
#
# result = {**dict_a, **dict_b, **dict_c}
# print(result)



# # Найдите три ключа с самыми высокими значениями в словаре
#
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# list = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(list)



# def solve(f):
#     n1 = f
#     n2 = int(str(f) * 2)
#     n3 = int(str(f) * 3)
#     n4 = n1 + n2 + n3
#     print(f"{n1} + {n2} + {n3} = {n4}")
#
#
# solve(20)
#
# result = lambda x: x + int(str(x) + str(x)) + int(str(x) + str(x) + str(x))
# print(result(20))

def calculate_structure_sum(data_structure):
    summa = 0
    # Прописываем условие при помощи цикла 1 summa для key и value
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
            # иначе выполняеться цикл 2 add к summa - список,кортэж,множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
            # иначе выполняеться действие 3 add к summa - целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
        # иначе выполняеться действие 4 add k summa - фу-цию len
    elif isinstance(data_structure, str):
        summa += len(data_structure)
        # возврат из функции значения summa
    return summa

# данные взятые из условия задачи
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# вывод результата программы
result = calculate_structure_sum(data_structure)
print(result)
