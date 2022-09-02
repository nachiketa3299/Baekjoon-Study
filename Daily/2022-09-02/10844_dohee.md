# 2022-09-01

# 백준 2630 색종이만들기

# 15 분 - 유형 재귀(top down)

# 코드 - 파이썬

```python
from collections import defaultdict,deque
from sys import setrecursionlimit, stdin; input = stdin.readline

setrecursionlimit(7000)

n = int(input().rstrip())
g = [[*map(int,input().split())] for _ in range(n)]

ans = [0,0]

def rec(y,x,siz):
    if siz == 1 or y+1==n or x+1==n : ans[ g[y][x] ] += 1
    else:
        pre = 0 if g[y][x] else 1
        flag = True
        for yy in range(y,y+siz):
            if pre in g[yy][x:x+siz]: flag = False; break
        if flag : ans[g[y][x]] += 1
        else :
            for yy in range(y,y+siz, siz//2):
                for xx in range(x,x+siz, siz//2): rec(yy,xx,siz//2)
    return

rec(0,0,n)
print(*ans, sep="\n")
```

# 풀이

재귀적으로 구현해줬습니다.
rec함수는 크게 두가지 경우로 나누어 작성했습니다.
(1) 지금 확인하려는 색종이 크기가 1인 경우
(2) 1보다 큰 siz 크기인 경우
(siz를 활용해서 슬라이싱으로 시작하는 좌표의 색상과 다른 색이 있나 확인하고, 다른 색이 없으면 그 색상으로 개수 하나 count해주고 리턴합니다. g[시작하는 좌표y][시작하는좌표 x]와 다른 색상이 확인하는 범위에 있을 경우, for문으로 rec(y + siz//2*i, x + siz//2*i, siz//2)로 다시 재귀적으로 더 작은 사이즈를 확인해주도록 합니다.)
