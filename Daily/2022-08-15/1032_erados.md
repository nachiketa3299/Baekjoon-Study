# 풀이시간
- 36분 30초

# 소스 코드

```python
n = int(input())

temp = [c for c in input()]

for i in range(1, n):
    new = input()
    temp = list(
        map(lambda x: x[1] if x[1] == new[x[0]] else "?", enumerate(temp))
    )

result = "".join(temp)
print(result)

```

# 풀이

첫 문자열을 temp list 로 만들고 새로 들어오는 문자열을 받을 때마다 각 문자 위치를 비교하여 다를 경우 temp 에 '?' 를 기록했다.

