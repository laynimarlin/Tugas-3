n = 7
for i in range(n):
    print(' ' * (n - i - 1) * 2, end='')
    print('* ' + '. ' * i, end='')
    print('* ' if i > 0 else '', end='') 
    print()
