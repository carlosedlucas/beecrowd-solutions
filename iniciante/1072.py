n = int(input())

lista_in = []
lista_out = []
for i in range(0, n):
    i = int(input())
    if 10 <= i <= 20:
        lista_in.append(i)
    else:
        lista_out.append(i)

print(f'{len(lista_in)} in')
print(f'{len(lista_out)} out')