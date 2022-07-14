time1 = int(input("Enter the time in seconds:"))
hours = time1 // 3600
minutes = (time1 % 3600) // 60
seconds = (time1 % 3600) % 60
print(hours, "hours", minutes, "minutes", seconds, "seconds")
