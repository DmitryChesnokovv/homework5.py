immutable_var = 1, 2, 3, True, "nutella"
print(immutable_var)
# immutable_var[0] = 6 #кортеж относится к неизменяемым типам данных/oшибка сообщает нам, что кортеж не поддерживает обращение по элементам!
mutable_list = [1, 2, 3, True, "nutella"]
print(mutable_list)
mutable_list[3] = 9
print(mutable_list)


print(immutable_var.__sizeof__())
print(mutable_list.__sizeof__())