# def count_nums_and_strings(data):
#     nums_sum = 0
#     strings_len = 0
#
#     for item in data:
#         if isinstance(item, int) or isinstance(item, float):
#             nums_sum += item
#         elif isinstance(item, str):
#             strings_len += len(item)
#         elif isinstance(item, (list, tuple)):
#             sub_nums_sum, sub_strings_len = count_nums_and_strings(item)
#             nums_sum += sub_nums_sum
#             strings_len += sub_strings_len
#         elif isinstance(item, dict):
#             sub_nums_sum, sub_strings_len = count_nums_and_strings(list(item.values()))
#             nums_sum += sub_nums_sum
#             strings_len += sub_strings_len
#
#     return nums_sum, strings_len
#
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# nums_sum, strings_len = count_nums_and_strings(data_structure)
#
# print("Сумма всех чисел:", nums_sum)
# print("Суммарная длина всех строк:", strings_len)


def calculate_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (list, tuple)):
            total_sum += calculate_sum(item)
        elif isinstance(item, dict):
            total_sum += calculate_sum(list(item.values()))

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}] )
]

result = calculate_sum(data_structure)
print(result)