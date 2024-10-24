#name = input('Введите имя: ')
#if name == 'Urban' :
 #   print('Здравствуйте, администратор')
#if name == 'Денис' :
 #   print('Здравствуйте, преподаватель')
#else :
 #   print('Привет', name)

number = int(input('Введите число:')) # Fizz, Buzz, FizzByzz
if number % 3 == 0 and number % 5 == 0:
    print("FizzByzz")
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print("Buzz")
else:
    print('Число не подходит')
