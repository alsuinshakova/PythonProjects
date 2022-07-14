my_string = input("Enter the world with space !!!- ").split()
for i, word in enumerate(my_string, 1):
    print(f'{i}). {word[:10]}')
