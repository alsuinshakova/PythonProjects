revenue = float(input("Введите значение выручки (тугрики) - "))
costs = float(input("Введите значение издержек (тугрики) - "))
result = revenue - costs
if result > 0:
    print(f"Поздравляю! Ваша компания работает с прибылью {result} тугриков!")
    print(f"Рентабельность выручки составила {100 * (result / costs):.1f}%")
    personal_n = int(input("Сколько счастливых целочисленных сотрудников работает в Вашей компании?"))
    print(f"Если Вы раздадите прибыль компании сотрудникам, то каждый получит по {result / personal_n:.3f} тугриков")
elif result < 0:
    print(f"Увы Ваша компания пока не сработала с убытком {-result} тугриков! Старайтесь, у Вас все получится!")
else:
    print("Ноль - это тоже хороший результат! Попросите у друга тугрик и пропейте его вместе за стабильность!")
