# 2022-09-14

# 백준 1865 웜홀

# 30 분 - 유형 벨만포드

# 코드 - 파이썬

```python
from collections import defaultdict,deque

global n,m,w,e
INF = int(2e9)

def BF(start):
    global n,m,w,e
    dis = [INF]*(n+1)
    dis[start] = 0

    for i in range(n):
        for edge in e:
            now = edge[0]
            nextt = edge[1]
            cost = edge[2]

            if dis[nextt] > cost+dis[now]:
                dis[nextt] = cost+dis[now]
                if i == n-1: return True
    return False


t = int(input().rstrip())
for _ in range(t):
    n,m,w = map(int, input().split())
    e = []

    for _ in range(m):
        s,ee,t = map(int, input().split())
        e.append((s,ee,t))
        e.append((ee,s,t))
    for _ in range(w):
        s,ee,t = map(int, input().split())
        e.append((s,ee,-t))
    flag = False
    for  i in range(1,n+1):
        if BF(i): flag = True;break
    if flag: print("YES")
    else: print("NO")
```

# 풀이

벨만포드 알고리즘을 통해 음의 사이클 존재 유무를 확인하는 원리를 활용했습니다.
