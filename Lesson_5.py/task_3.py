
def workers_statistics():
    workers = [['Морозова ', '12000 \n'], ['Петрова ', '19000 \n'], ['Кравцева ', '145000 \n'], ['Смирнов ', '80000']]
    try:
        with open('test.txt', 'r+', encoding="utf-8"):
            for i in range(len(workers)):
                file. writelines(workers[i])
            l = file. readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'

workers_statistics()