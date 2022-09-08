def sun(n_1, n_2):
    try:
        n_1, n_2 = float(n_1), int(n_2)
        sun_num = n_1 / n_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return round(sun_num, 4)


print(sun(input("Введите числитель- "), input("Введите второе число- ")))
