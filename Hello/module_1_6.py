my_dict = { "Denis" : 1996, 'Blad': 1985, 'Masha' : 2001 }
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Oleg'))
my_dict.update({'Kirill' : 2004,
                "Lera" : 1985})
a = my_dict.pop('Masha')
print(a)
print(my_dict)
my_set = {'Lemon', 'Lemon', 1,1, 45, 45, 'potato', 'potato', 12,12, 33, 33, 'Juice' }
print(my_set)
my_set.add('Coffe Tea')
my_set.discard(45)
print(my_set)

