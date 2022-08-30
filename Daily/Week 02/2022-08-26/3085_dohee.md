# 2022-08-25

# 백준 3085 사탕게임

# ? 분 - 실패

# 코드 - 파이썬

```python

from collections import defaultdict, deque
global n, ans
ans = 0
n = int( input().rstrip() )
g = []
for _ in range(n):
    st = input().rstrip()
    g.append(list(st))

dir = [(0,1),(1,0),(-1,0),(0,-1)]

four = [[(0,1),(0,-1)],[(1,0), (-1,0)] ]
def candy(arr):
    global n, ans
    for l in arr:
        y,x = l
        ch = g[y][x]
        for dd in four:
            total = 0
            for d in dd:
                cnt = 1
                ny,nx = y+d[0], x+d[1]
                while ny>0 and ny<n and nx>0 and nx<n:
                    if g[ny][nx]!=ch:break
                    cnt+=1
                    ny, nx = ny+d[0], nx+d[1]
                total+=cnt
            if total>ans: ans = total
for y in range(n):
    for x in range(n):
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>= n: continue
            if g[y][x] != g[ny][nx]:
                c1, c2 = g[y][x], g[ny][nx]
                g[y][x], g[ny][nx] = g[ny][nx],g[y][x]
                candy([(y,x),(ny,nx)])
                g[y][x], g[ny][nx] = g[ny][nx],g[y][x]
print(ans)


```

# 풀이

실패 - 디버깅중
