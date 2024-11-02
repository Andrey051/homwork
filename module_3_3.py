def print_params(a=1, b='строка', c=True):  # *args, **kwargs
    print(a, b, c)
print_params()
print()

print_params(4, 'string', 2.3)
print_params(False, True)
print_params(a=3, b='s', c=2.3)
print_params(a='None', b='True')
print_params(a='None', c='w')
print_params(b='q')

print_params(b=25)
print_params(c=[1, 2, 3, ])
print()

values_list = [2.2, False, "string"]
value_dict = {'a': 'None', 'b': 34, 'c': False}
print_params(*values_list)
print_params(**value_dict)
print()

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)
print()
