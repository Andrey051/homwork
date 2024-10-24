first = input('Числа 1: ')
second = input('Число 2: ')
third =input('Число 3: ')

if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')