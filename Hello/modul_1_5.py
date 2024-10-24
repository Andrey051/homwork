immutable_var = 1, 2, 3, True, 'string'
print(immutable_var)
print(type(immutable_var))
#immutable_var[0] = 111 (не возможно поменять данные в кортеже - это его особенность)
mutable_list = [1, 4, 6, 'Modified']
print(mutable_list)
print(type(mutable_list))