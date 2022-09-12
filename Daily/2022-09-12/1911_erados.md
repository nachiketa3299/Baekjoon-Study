# 시간
- 19분

# 풀이
- 널빤지 위치를 정렬하고 이전에 놓은 널빤지 끝과 지금 매꿀 웅덩이 시작 지점중 큰 걸 새 시작점으로 하여 필요한 널빤지 수를 구하고 널빤지 끝 위치를 갱신했다. 


# 코드

```python
from math import ceil
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
cnt = 0
last = 0
holes = []

for _ in range(N):
    A, B = map(int, input().split())
    holes.append((A, B))
holes.sort()

for s, e in holes:
    s = max(last, s)
    n = ceil((e - s) / L)
    last = s + n * L
    cnt += n

print(cnt)

```