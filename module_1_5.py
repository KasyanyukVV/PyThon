immutable_va = 1870, "Ленин", 1878, "Сталин"
print(immutable_va)
# mmutable_va [0] = 1878 # tuple является не изменяемым в отличии от list
print(type(immutable_va))

mutable_list = ["ABC", "СССР", 1, "Ленин", 2, "Сталин"]
print(mutable_list)
mutable_list[0] = "Вожди"
print(mutable_list,type(mutable_list))