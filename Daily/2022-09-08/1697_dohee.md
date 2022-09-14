# 2022-09-14

# 백준 1238 파티

# 10분 - 유형 BackTracking

# 코드 - Python

```python
from collections import defaultdict,deque
import heapq as hq


global n,m,x,INF
INF = int(2e9)

n,m,x = map(int ,input().split())
go = [[] for _ in range(n)]
back = [[] for _ in range(n)]
for i in range(m) :
    s,e,t = map(int, input().split())
    s,e = s-1,e-1
    back[s].append((e,t))
    go[e].append((s,t))

g = [INF]*n
b = [INF]*n

def dijk(g, dist):
    global n,m,x
    dist[x-1] = 0
    q = []
    hq.heappush(q,(0,x-1))
    while q:
        nowc, now = hq.heappop(q)
        if nowc > dist[now]: continue
        for l in g[now]:
            node,c = l
            cost = c+nowc
            if dist[node] > cost:
                dist[node] = cost
                hq.heappush(q,(cost,node))

    return dist


g = dijk(go,g)
b = dijk(back,b)
ans = 0
for i in range(n) : ans = max(ans, g[i]+b[i])

print(ans)
```

# 풀이

컨셉을 쉽게 설명하자면,
다익스트라의 원리를 이용했습니다.
