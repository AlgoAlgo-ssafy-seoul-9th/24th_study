import sys
input = sys.stdin.readline

def dot_check(distance, dot_cordi, n, m):
    cnt = 1
    before = dot_cordi[0]

    for i in range(1, n):
        if dot_cordi[i] - before >= distance:
            cnt += 1
            before = dot_cordi[i]
    
    if cnt >= m:
        return True
    else:
        return False

N, M = map(int, input().split())
dots = list(map(int, input().split()))

dots.sort()

i, j = 1, dots[-1]-dots[0]

ans = 0
while i <= j:
    mid = (i+j)//2

    if dot_check(mid, dots, N, M):
        ans = mid
        i = mid + 1
    else:
        j = mid - 1

print(ans)