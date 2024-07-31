my_dict = {"Ленин": 1870, "Сталин": 1878, "Путин": 1952,}
print(my_dict)
print(my_dict.get("Ленин"))
print(my_dict.get("Ельцежоп"))
my_dict.update({"Гейб Ньюэлл": 1962,
                "Крис Метцен": 1973})
del my_dict["Путин"]
print(my_dict)

print()

my_set = {"Rip", 69, 66.6, True, 228, 69, 228, True, (69, 228, 99.9)}
print(my_set)
print(my_set.add(777))
print(my_set.add(1870))
print(my_set.discard(66.6))
print(my_set)
