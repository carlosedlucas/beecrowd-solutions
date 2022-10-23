from math import gcd

n = int(input())

for i in range(0, n):
    n1, n2 = map(int, input().split(" "))
    mdc = gcd(n1, n2)
    print(mdc)