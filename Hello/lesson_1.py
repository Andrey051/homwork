a = 2
a = 4
print(a)
a = b = c = 0
# print(a,b,c)
# print(id(a), id(b), id(c))
a, b, c = 1, 2, 3
print(id(a), id(b), id(c))
a, d = 1, 2
print(a, b)
a, b = b, a
print(a, b)
print(type(a))
