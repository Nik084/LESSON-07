team1_name = '"Мастера кода"'
team2_name = '"Волшебники данных"'
team1_num = 5
team2_num = 6
score1 = 40
score2 = 47
team1_time = 1552.512
team2_time = 2153.31
tasks_total = score1 + score2
time_avg = round(((team1_time + team2_time)/tasks_total),2)

# Определим победителя, критерий: кто меньше тратил время на решение одной задачи
if score1/team1_time > score2/team2_time:
    challenge_result = f'Победа команды {team1_name}!'
elif score1/team1_time < score2/team2_time:
    challenge_result = f'Победа команды {team2_name}!'
else:
    challenge_result = "Ничья!"

# использование %
print('Название первой команды: %s' % team1_name)
print('в команде %s участников: %s' % (team1_name, team1_num))
print('Количество участников в командах: %s и %s' % (team1_num, team2_num))

# использование format()
print('Название второй команды: {}'.format (team2_name))
print('Количество задач, решенных командой {}: {}'.format (team2_name, score2))
print('{} решили задачи за {} с'.format (team2_name, team2_time))

# использование f-строк
print(f'Команды решили {score1} и {score2} задач')
print(f'Суммарно сегодня было решено {score1 + score2} задач, в среднем по {time_avg} секунды на одну задачу!')
print(f'Результат битвы: {challenge_result}')










