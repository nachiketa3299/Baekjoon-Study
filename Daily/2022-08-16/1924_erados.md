# 시간
- 10분

# 코드
```python
m, d = map(int, input().split())

temp = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5, 1]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

print(days[(d + temp[m - 1]) % 7])
```

# 풀이
전월까지의 날짜들을 7로 나눈 나머지를 저장해두고 오늘 날짜랑 더해서 mod 7 했다.
