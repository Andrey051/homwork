def calculate_average(grades, students):
    averages = {}
    for i in range(len(grades)):
        total = sum(grades[i])
        average = total / len(grades[i])
        averages[list(students)[i]] = average
    return averages

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

averages = calculate_average(grades, students)

for student, average in averages.items():
    print(f'{student}: {average}')