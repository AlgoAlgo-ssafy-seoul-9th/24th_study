import sys
input = sys.stdin.readline

def sol(dis):
    cnt = 1
    before = spots[0]
    for i in range(1, N):
        if before + dis <= spots[i]:     # i에서 dis 만큼 떨어진 거리보다 i+1이 크면
            cnt += 1
            before = spots[i]
    return cnt

N, M = map(int, input().split())
spots = list(map(int, input().split()))
spots.sort()

i, j = 1, spots[-1] - spots[0]
while i <= j:
    mid = (i+j) // 2

    if sol(mid)>= M:        # cnt가 목표보다 크다는 것은 간격을 너무 작게 뛴다는 뜻
        ans = mid
        i = mid + 1
    else:
        j = mid - 1
print(ans)

