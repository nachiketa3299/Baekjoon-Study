# 2022-08-25

# 백준 미로탐색

# 15분 - 유형 BFS

# 코드 - Python

```python

from collections import defaultdict, deque
global n,m,g,visit
n,m = map(int, input().split())
g = [ input().rstrip() for _ in range(n)]

dir = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs():
    global n,m,g
    visit = [ [0]*m for _ in range(n)]
    q = deque(); visit[0][0] = 1; q.append((0,0))
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = d[0]+y, d[1]+x
            if ny<0 or nx<0 or ny>=n or nx>=m: continue
            if ny==n-1 and nx == m-1: print(visit[y][x]+1); exit(0)
            if visit[ny][nx]>0 or g[ny][nx] == '0': continue
            visit[ny][nx] = visit[y][x] + 1
            q.append((ny,nx))
bfs()



```

#풀이
전형적인 BFS 문제
이차원배열 visit[y][x]에 (0,0)에서부터 (y,x)까지 도달하기 위한 최단 거리를 저장함
