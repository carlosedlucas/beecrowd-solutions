a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a, b, c, d, e]
count_odd = []

count_pairs = list(filter(lambda x: True if x % 2 == 0 else False, lista))
count_odd = list(filter(lambda x: True if x % 3 == 0 else False, lista))
print(f'{len(count_pairs)} valor(es) par(es)')
print(f'{len(count_odd)} valor(es) impar(es)')