my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # список
index = 0                                              # индекс элемента списка
while index < len(my_list) :
    if my_list[index] > 0:
        print(my_list[index], 'Число больше ноля ')
    elif  my_list[index] < 0:
        break
    index = index + 1