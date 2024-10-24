set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2 ,3)}
list_ = [1, 1, 1, 1, 2, 3, 2, 2]
list_ = set(list_)
print(list_)
print(list_.discard(1))
print(list_)
print(list_.add(5))
print(list_)