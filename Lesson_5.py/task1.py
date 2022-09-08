with open('task_1.py', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done:')
        if not line:
            break
        # f.write(f"{line}/n")
        print(line, file=f)