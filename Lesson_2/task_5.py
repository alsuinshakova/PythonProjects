my_list = [5, 4, 4, 3, 2, 1]
new_number = ""
while new_number != "q":
    i = 0
    new_number = input("Enter a new rating! element in the form of a natural number.\nTo exit - q\n ")
    if new_number.isdigit():
        for n in my_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(new_number))
    print(my_list)
