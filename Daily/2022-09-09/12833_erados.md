# 시간
- 9 분

# 풀이
- XOR B 를 2번 하면 원래 수가 된다.

# 코드
```python
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

if C % 2 :
    print(A^B)
else:
    print(A)
```