phone_book = {'Denis' : 89112223334, 'Max' : 89114433551}
print(phone_book)
print(phone_book['Denis'])
phone_book['Denis'] = 8999232445
phone_book['Anton'] = 8911987465
print(phone_book)
del phone_book['Max']
print(phone_book)
phone_book.update({'Sasha': 8923441123,
                   'Alex': 8921455654})
print(phone_book)
print(phone_book.get('Denis'))
print(phone_book.get('Kamila'))
print(phone_book.get('Kamila', 'Такого ключа нет'))
print(phone_book)
phone_book.pop('Anton')
print(phone_book)
a = phone_book.pop('Denis')
print(a)
list_ = [1, 2, 3]
list_.pop(0)
print(list_)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())