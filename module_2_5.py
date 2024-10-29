def get_matrix(n, m, value):
    matrix = []   # Создаём пустой список matrix внутри функции get_matrix
    for i in range(n):  #Пишем первый (внешний) цикл for для количества строк матрицы, n повторов
        matrix.append([])  #   В первом цикле добавляем пустой список в список matrix
        for j in range(m):   # Пишем второй (внутренний) цикл for для количества столбцов матрицы, m повторов
            matrix[i].append(value)   # Во втором цикле пополняем ранее добавленный пустой список значениями value
    return (matrix)   # После всех циклов возвращаем значение переменной matrix
    print(get_matrix())
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

