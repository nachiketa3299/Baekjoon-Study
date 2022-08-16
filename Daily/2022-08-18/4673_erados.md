# 풀이시간
- 19분 19초


# 풀이
d(x) > x 이다. d(x) 를 각 x in range(1, 10000) 에 대해 한 번만 호출하면 10000 이하의 모든 생성자가 존재하는 수를 찾을 수 있다.
그래서 거기 없는 값만 필터링했다.

# 코드
```python
index = {}


def d(n):
    return n + sum([int(i) for i in str(n)])


for i in range(1, 10000):
    index[str(d(i))] = True

print(
    "\n".join(
        list(
            filter(
                lambda x: not index.get(str(x)),
                map(lambda x: str(x), range(1, 10000)),
            )
        )
    )
)
```