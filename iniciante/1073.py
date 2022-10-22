n = int(input())

if n % 2 == 0:
    for i in range(2, n + 1, 2):
        print(f'{i}^2 = {pow(i, 2):.0f}')
else:
    for i in range(2, n, 2):
        print(f'{i}^2 = {pow(i, 2):.0f}')
