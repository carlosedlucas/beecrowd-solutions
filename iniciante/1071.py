x = int(input())
y = int(input())

lista = []
if x % 2 == 0:
        for i in range(x-1, y, -2):
                lista.append(i)
        resultado = sum(lista)
        print(resultado)
else:
        for i in range(x-2, y, -2):
                lista.append(i)
        resultado = sum(lista)
        print(resultado)