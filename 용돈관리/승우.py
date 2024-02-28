import sys
input = sys.stdin.readline

N, M = map(int, input().split())

spend_list = [int(input()) for _ in range(N)]

s = max(spend_list)
e = 1000000001
answer = 0

while s <= e:
    cnt = 1
    mid = (s + e) // 2
    cur = mid
    for i in range(N):
        spend = spend_list[i]
        if cur >= spend:
            cur -= spend
        else:
            cur = mid - spend
            cnt += 1
    
    if cnt <= M:
        answer = mid
        e = mid - 1
    else:
        s = mid + 1

print(answer)


