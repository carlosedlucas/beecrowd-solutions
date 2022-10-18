dias = int(input())

resto = 0
ano = 0
while dias >= 365:
    resto = dias % 365
    dias -= 365
    ano += 1

mes = 0
while dias >= 30:
    resto = dias % 30
    dias -= 30
    mes += 1

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')