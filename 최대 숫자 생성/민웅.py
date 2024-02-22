import sys
input = sys.stdin.readline

N = int(input())

num_lst = []

for _ in range(N):
    tmp = input().strip()
    l = len(tmp)
    num_tmp = tmp*10
    num_tmp = num_tmp[:10]
    num_lst.append([num_tmp, l])


num_lst.sort(key=lambda x: x[0], reverse=True)

ans_lst = []
for v in num_lst:
    ans_lst.append(v[0][:v[1]])
print(''.join(ans_lst))