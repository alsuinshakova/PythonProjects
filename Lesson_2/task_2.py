my_list = input("Введите число -").split()
for i in range(1, len(my_list) // 2, 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)
