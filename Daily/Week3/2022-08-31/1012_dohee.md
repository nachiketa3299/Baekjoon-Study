# 2022-08-31

# 백준 1012 유기농배추

# 30분 - 유형 BFS/DFS

# 코드 - Python

```python
from collections import deque
global k,n,m
t = int(input().rstrip())
gg = []
dir = [(0,1),(1,0),(-1,0),(0,-1)]
k,n,m = 0,0,0
def dfs(y,x):
    global k,n,m
    k-=1
    if k == 0: return
    for d in dir:
        ny,nx = d[0]+y, d[1]+x
        if ny<0 or nx<0 or ny>=n or nx>=m: continue
        if g[ny][nx] :
            g[ny][nx] = 0
            dfs(ny,nx)

for tt in range(t):
    m,n,k = map(int,input().split())
    g = [[0]*m for _ in range(n)]
    ans = 0
    bachoo = deque([])
    for _ in range(k):
        x,y = map(int,input().split())
        g[y][x] = 1
        bachoo.append((y,x))

    for b in bachoo:
        if g[b[0]][b[1]] == 1:
            ans+=1
            g[b[0]][b[1]] = 0
            dfs( b[0], b[1])
            if k == 0: break
    print(ans)
```

# 풀이

전형적인 dfs(bfs)문제입니다.
처음에 문제는 빠르게 풀었으나 예상치 못한 곳에서 계속 에러가 발생해서
3번 새로 코드를 작성했네요
TypeError: 'bool' object does not support item assignment
라는 에러가 났었습니다.
