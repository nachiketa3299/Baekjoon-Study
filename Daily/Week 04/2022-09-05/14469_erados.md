# 시간
- 14분

# 풀이
- 처음엔 sort 없이 풀어보려고 했는데 복잡도가 오히려 증가해서 별론 것 같다.
- map 후 * 를 사용하면 map object 말고 map 의 결과를 얻을 수 있다.

# 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
max_time = 0
data = sorted([[*map(int,input().split())] for _ in range(N)])

for i in range(N):
    start, delay = data[i]
    if max_time > start:
        max_time += delay
    else:
        max_time = start + delay

print(max_time)
```