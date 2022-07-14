while True:
    days = 1
    start_km = float(input("Стартовый результат:"))
    last_km = float(input("Финальный результат:"))
    if start_km <= 0 or last_km < 0:
        print("Результаты должны быть больше нуля, стартовое значение!= 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print(f"Спортсмен добьется результата за {days} дней")
        break
