from math import factorial


def factorial_gen(n):
    temp = 1
    for i in range(1, n + 1):
        print(i, end='! = ')
        yield factorial(i)


print("<<Программа вычисления факториала числа>>")
for el in factorial_gen(15):
    print(el)
