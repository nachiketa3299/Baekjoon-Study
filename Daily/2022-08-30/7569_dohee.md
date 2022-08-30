# 2022-08-30

# 백준 7569 토마토 X

# 60 분 - 유형 bfs (실패)

# 코드 - 파이썬

```python

import sys
from collections import deque
m,n,h = map(int,input().split())
graph = []
q = deque([])
ts,red,ans =0,0,0

for i in range(h):
    l = []
    for j in range(n):
        l.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if l[j][k]!=-1:
                ts+=1
            if l[j][k]==1:
                red +=1
                q.append([i,j,k])
    graph.append(l)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
ts -= red
while(q):
    x,y,z = q.popleft()

    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            ts-=1
            q.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            ans = graph[x][y][z]

if ts == 0: print(ans)
else: print(-1)

```

# 풀이

(실패)
BFS
3차원 배열로 풀어야하는 기본적인 BFS 문제

해당 문제를 풀다가 어디선가 코드가 꼬여서 시간이 매우 오래걸림.
