immutable_var = 1, True, 0.1, "Swiat"
print("Immutable tuple:", immutable_var)

#immutable_var[0] = 45 - Неверно, так как главное отличие кортежа от списка - это неизменяемость

mutable_list = list(immutable_var)
mutable_list.append("Urban")
print("Mutable list:", mutable_list)
