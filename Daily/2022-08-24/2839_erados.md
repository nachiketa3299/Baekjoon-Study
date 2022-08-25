# 시간
- 9분

# 풀이
5kg 짜리가 많으면 되므로 5로 먼저 나눈 뒤 나머지를 가지고 5kg 봉지를 줄이고 3kg봉지를 늘렸다.

# 소스
```python
n = int(input())

a = n // 5 - (n % 5) % 3
b = (n % 5 * 2) % 5
print(-1 if a < 0 else a + b)

```