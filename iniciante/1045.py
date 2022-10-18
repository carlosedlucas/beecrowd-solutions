X, Y, Z = map(float, input().split(" "))

lista = sorted([X, Y, Z])
A = lista[-1]
B = lista[-2]
C = lista[-3]

if A >= B+C:
    print('NAO FORMA TRIANGULO')
elif (A**2) == (B**2)+(C**2):
    print('TRIANGULO RETANGULO')
elif (A**2) > (B**2)+(C**2):
    print('TRIANGULO OBTUSANGULO')
    if A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')
elif (A**2) < (B**2)+(C**2):
    print('TRIANGULO ACUTANGULO')
    if A == B and A == C and B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')
elif A == B or A == C or B == C:
    print('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO EQUILATERO')