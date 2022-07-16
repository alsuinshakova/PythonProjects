time = int(input("Enter the time in seconds:"))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(hours, "hours", minutes, "minutes!", seconds, "seconds")
