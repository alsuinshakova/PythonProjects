num = int(input("Введите целое положительное число: "))
a = 0
n = num
while n > 0:
    b = n % 10
    if b > a:
        a = b
        if a == 9:
            break
    n = n // 10
print(f"Наибольшая цифра в числе {num} равна {a}!")
