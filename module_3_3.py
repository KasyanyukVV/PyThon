def print_params(a = 1, b = 'строка', c = True):
    print("Параметр а:", a)
    print("Параметр b:", b)
    print("Параметр c:", c)

print_params()
print("-----------------------")
print_params(10, 'новая строка', False)
print("-----------------------")
print_params(b=25)
print("-----------------------")
print_params(c=[1, 2, 3])
print("-----------------------")
values_list = [1, 2.1, 'lOL']
print_params(*values_list)
print("-----------------------")
values_dict = {'a': 45, 'b': 19.5, 'c': "Хай"}
print_params(**values_dict)
print("-----------------------")
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42 )