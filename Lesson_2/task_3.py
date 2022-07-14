seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month_num = int(input('Введи номер! месяца(только цифра): '))
if month_num in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
            break
