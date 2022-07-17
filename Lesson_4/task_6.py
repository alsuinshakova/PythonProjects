from itertools import count, cycle

for i in count(3):
    if i == 10:
        break
    print(i)

user_cycle = cycle(['один', 'два', True, None, {'dict': False}])
for i in range(20):
    print(next(user_cycle))
