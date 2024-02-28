# 6236_용돈관리
import sys
input = sys.stdin.readline

def bs(mid_value):
    cnt = 0
    deposit = 0
    for k in range(N):
        if deposit < s_lst[k]:
            deposit = mid_value
            cnt += 1
            deposit -= s_lst[k]
        else:
            deposit -= s_lst[k]

    if cnt <= M:
        return False
    else:
        return True


N, M = map(int, input().split())

s_lst = []

for _ in range(N):
    s_lst.append(int(input()))

# 초기값, 최소 = 하루사용해야하는 최대값, 최대 = 전체합
i = max(s_lst)
j = sum(s_lst)
ans = 0
while i <= j:
    mid = (i+j)//2

    if bs(mid):
        # 필요 횟수보다 더 많은횟수 뽑아야하면 인출금액 올리기
        i = mid+1
    else:
        # 필요한 횟수보다 작거나 같으면 정답갱신 및 최대값 줄이기
        ans = j
        j = mid-1


print(ans)

