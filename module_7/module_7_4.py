# -*- coding: utf-8 -*-


def main():
    # Пример входных данных
    team1_num = 5                          # количество участников первой команды
    team2_num = 6                          # количество участников второй команды
    score_1 = 40                           # количество решённых задач первой команды
    score_2 = 42                           # количество решённых задач второй команды
    team1_time = 1552.512                  # время за которое решила задачи команда 1
    team2_time = 2153.31451                # время за которое решила задачи команда 2
    tasks_total = sum((score_1, score_2))  # количество задач
    time_avg = round((sum((team1_time, team2_time)) / tasks_total), 1)  # среднее время решения
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = 'Победа команды Волшебники Данных!'
    else:
        challenge_result = 'Ничья!'

    # Использование %:
    print('В команде Мастера кода участников: %s!' % team1_num)
    print('Итого сегодня в командах участников: %s и %s!'% (team1_num, team2_num))

    # Использование format():
    print('Команда Волшебники данных решила задач: {}!'.format(score_2))
    print('Волшебники данных решили задачи за {:.1f} с!'.format(team1_time))

    # Использование f-строк:
    print(f'Команды решили {score_1} и {score_2} задач.')
    print(f'Результат битвы: {challenge_result}')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


if __name__ == '__main__':
    main()

