# 시간 
- 24분(실패)

# 풀이
- 로직은 맞는데 
```python
    a = list(filter(lambda x: x % i != 0 or x == i, a))
```
여기가 좀 오래걸리는 것 같다.

# 코드
```python
from math import sqrt, ceil


m, n = map(int, input().split())

a = [i for i in range(m, n + 1)]

for i in range(2, ceil(sqrt(n)) + 1):
    a = list(filter(lambda x: x % i != 0 or x == i, a))

print("\n".join(map(str, a)))
```
