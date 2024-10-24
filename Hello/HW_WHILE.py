while 1 > 0:  # в место 1 > 0 можно ввести True, с этим значением будет тоже самое
    number = int(input('Введите число'))
    if number % 2 == 0:
        print('Число четное')
        continue
    else:
        print('Число нечетное')
    print('Меня не забыли')
print('Я за циклом')
