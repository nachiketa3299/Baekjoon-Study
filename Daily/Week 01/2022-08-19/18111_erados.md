# 시간 
- 25분(실패)

# 풀이
- 주말에 좀 더 해봐야겠다..

# 코드

```python
n, m, b = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]

avg = sum([sum(i) for i in a]) / n / m
height = round(avg)

# 쌓을 블록 수
up = 0

# 뺄 블록 수
down = 0
for i in range(n):
    for j in range(m):
        diff = height - a[i][j]
        if diff > 0:
            up += height - a[i][j]
        else:
            down -= diff
while b + down < up:
    down += down
ans = 2 * down + up


print(avg)
```