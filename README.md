# 24th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [두 용액](https://www.acmicpc.net/problem/2470)

### [민웅](./두%20용액/민웅.py)

```py

```

### [병국](./두%20용액/병국.py)

```py

```

### [상미](./두%20용액/상미.py)

```py


```

### [성구](./두%20용액/성구.py)

```py

```

### [승우](./두%20용액/승우.py)

```py


```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [최대 숫자 생성](https://www.codetree.ai/problems/maximum-number-generation/description)

### [민웅](./최대%20숫자%20생성/민웅.py)

```py
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
```

### [병국](./최대%20숫자%20생성/병국.py)

```py


```

### [상미](./최대%20숫자%20생성/상미.py)

```py
def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x : x*10, reverse=True)
    answer = ''.join(numbers)

    return answer

n = int(input())
arr = [input() for _ in range(n)]
print(solution(arr))

```

### [성구](./최대%20숫자%20생성/성구.py)

```py

```

### [승우](./최대%20숫자%20생성/승우.py)

```py


```

## [올바른 쌍의 괄호](https://www.codetree.ai/problems/valid-pair-of-parentheses/description)

### [민웅](./올바른%20쌍의%20괄호/민웅.py)

```py
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
```

### [병국](./올바른%20쌍의%20괄호/병국.py)

```py


```

### [상미](./올바른%20쌍의%20괄호/상미.py)

```py
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

```

### [성구](./올바른%20쌍의%20괄호/성구.py)

```py

```

### [승우](./올바른%20쌍의%20괄호/승우.py)

```py


```

## [멀리멀리](https://www.codetree.ai/problems/far-away/description)

### [민웅](./멀리멀리/민웅.py)

```py
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
```

### [병국](./멀리멀리/병국.py)

```py


```

### [상미](./멀리멀리/상미.py)

```py
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



```

### [성구](./멀리멀리/성구.py)

```py

```

### [승우](./멀리멀리/승우.py)

```py


```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
