# 시간
- 20분

# 풀이
- 첨에는 정렬 없이 브루트포스로 풀려고 했다가 시간초과났다.
- 투 포인터가 참으로 효율적이구나


# 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
data = sorted([*map(int, input().split())])
X = int(input())

cnt = 0
left = 0
right = N - 1

while left < right:
    temp = data[left] + data[right]
    if temp == X:
        cnt += 1
        left += 1
    elif temp < X:
        left += 1
    elif temp > X:
        right -= 1

print(cnt)
```