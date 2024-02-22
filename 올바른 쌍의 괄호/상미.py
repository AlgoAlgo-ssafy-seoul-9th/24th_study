import sys
input = sys.stdin.readline

bracket = input().strip()
cnt = 0
ans = 'Yes'
for b in bracket:
    if b == '(':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        ans = 'No'
        break
else:
    if cnt != 0:
        ans = 'No'
print(ans)