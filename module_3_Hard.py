
def calculate_structure_sum(data):
    total_sum = 0

    # Если data - это список,кортэж,множества проходим по его элементам
    if isinstance(data, (tuple, list, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)

    # Если data - это словарь, проходим по его ключам и значениям
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    # Если data - это строка, добавляем её длину
    elif isinstance(data, str):
        total_sum += len(data)

    # Если data - это число, добавляем его значение
    elif isinstance(data, (int, float)):
        total_sum += data

    # Если data - это другой тип, игнорируем его
    return total_sum


# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)