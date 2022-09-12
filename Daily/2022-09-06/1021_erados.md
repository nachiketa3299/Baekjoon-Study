# 시간
- 25분

# 풀이
- 현재 내 위치와 타겟 위치 사이의 거리는 두 개가 있는데 그 중 작은 걸 선택해나가면 된다.


# 코드

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

queue = list(map(int, input().split()))
arr = list(range(1,N+1))
cnt = 0
curr = 0
i = 0
for n in queue:
    idx = arr.index(n)
    cnt += min(abs(idx - curr), N - abs(idx - curr)- i)
    arr.pop(idx)
    curr = idx
    i += 1
print(cnt)
```