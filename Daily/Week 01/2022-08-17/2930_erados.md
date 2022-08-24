# 시간
- 53분 52초 (Fail)

# 코드
```python
score_table = {
    "R": {
        "R": 1,
        "S": 2,
        "P": 0,
    },
    "S": {
        "R": 0,
        "S": 1,
        "P": 2,
    },
    "P": {
        "R": 2,
        "S": 0,
        "P": 1,
    },
}

r = int(input())
a = [c for c in input()]
n = int(input())
b = [input() for _ in range(n)]
b = list(map(list, zip(*b)))
b = [
    {"R": b[i].count("R"), "S": b[i].count("S"), "P": b[i].count("P")}
    for i in range(r)
]
print(
    sum(
        [
            sum([score_table[i][k] * j[k] for k in j.keys()])
            for i, j in zip(a, b)
        ]
    )
)

print(
    sum(
        [
            sum([k[1] * i for i, k in enumerate(item)])
            for item in [sorted(i.items(), key=lambda item: item[1]) for i in b]
        ]
    )
)


```
# 풀이
손 가는 대로 풀었다. 샘플들에 대해서는 맞는데 틀렸다고 뜬다.
행렬을 tanspose 할 때 
```python
map(list, zip(*a))
```
이렇게 하면 된다.