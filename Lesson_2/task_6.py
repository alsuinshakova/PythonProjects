goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица  измерения': ''}
analytics = {'название': [], 'цена': [], 'количество!': [], 'единица  измерения': []}
num =0
while True:
    if input('Для выхода из программы нажмите "q", для продолжения "Enter: '). upper() == 'q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        answer = input(f' Введите значение свойства "{f}":')
        f_copy[f] = int(
            answer)if f in 'цена количества' and answer.isdigit() else answer
        analytics[f].append(f_copy[f])
        goods.append((num, f_copy))
        print(f"\nСтруктура товаров\n{goods}")
        print(f'\n Текущая аналитика по товарам: \n {"*" * 50}')
        for key, value in analytics.items():
            print(f'{key:>50}:{value}')
        print("*" * 50)

