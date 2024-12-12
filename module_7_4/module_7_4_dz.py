team1_num = 5  # количество участников первой команды
team2_num = 6  # количество участников второй команды
score_1 = 55  # количество задач решённых командой 1
score_2 = 54  # количество задач решённых командой 2
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82  #количество решённых задач всего
time_avg = 45.2


print("В команде Мастера кода участников: %s !" % team1_num )
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print(f"Команды решили {score_1} и {score_2} задач.")




if score_1 > score_2 and score_1 == score_2 and team1_time > team2_time:
    print(f"Победа команды Мастера кода!")
elif score_1 < score_2 and score_1 == score_2 and team1_time < team2_time:
    print(f"Победа команды Волшебники Данных!")
else:
    print("Ничья!")

tasks_total = score_1 + score_2

time_avg = (team1_time + team2_time) / tasks_total
print(f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!.")

