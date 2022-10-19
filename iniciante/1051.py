x = float(input())

if x <= 2000.00:
    print('Isento')
elif 2000.00 < x <= 3000.00:
    imp8 = (x - 2000) * 0.08
    imp = imp8
    print(f'R$ {imp:.2f}')
elif 3000.00 < x <= 4500.00:
    imp8 = 80.00
    imp18 = (x - 3000) * 0.18
    imp = imp8 + imp18
    print(f'R$ {imp:.2f}')
else:
    imp8 = 80.00
    imp18 = 270.00
    imp28 = (x - 4500) * 0.28
    imp = imp8 + imp18 + imp28
    print(f'R$ {imp:.2f}')
