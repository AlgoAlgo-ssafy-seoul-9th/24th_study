import sys
input = sys.stdin.readline

brackets = list(input().strip())

l = len(brackets)
stack = []

idx = 0
ans = ''
while True:
    if idx == l:
        break
    tmp = brackets[idx]
    if stack:
        if tmp == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                ans = "No"
                break
        else:
            stack.append(tmp)
    else:
        if tmp == ')':
            ans = "No"
            break
        stack.append(tmp)
    
    idx += 1

if ans != 'No':
    if stack:
        print("No")
    else:
        print("Yes")
else:
    print(ans)