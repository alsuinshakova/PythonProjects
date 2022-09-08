num = input("Ввести число: ")
print(True if num.replace("-","").isdigit() else False)