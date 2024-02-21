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

```

### [병국](./최대%20숫자%20생성/병국.py)

```py


```

### [상미](./최대%20숫자%20생성/상미.py)

```py


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
