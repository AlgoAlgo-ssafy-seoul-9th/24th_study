## 백준_ 2470_ 두 용액

import sys 
input = sys.stdin.readline

N = int(input())
solu = list(map(int, input().split()))

solu.sort(key=lambda x: abs(x))
tmp = 10000000000
a, b = -1000000000, 1000000000
for i in range(N-1):
    dif = abs(solu[i+1] + solu[i])
    if abs(dif) <= tmp:
        tmp = abs(dif)
        a, b = solu[i], solu[i+1]
if a > b:
    a, b = b, a
print(a, b)
    