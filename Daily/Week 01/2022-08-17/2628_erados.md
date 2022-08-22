# 시간
- 9분 55초

# 코드
```python
c, r = map(int, input().split())
n = int(input())
a = [[0], [0]]

for i in range(n):
    d, k = map(int, input().split())
    a[d].append(k)

a[0].append(r)
a[1].append(c)
a[0].sort()
a[1].sort()

print(
    max([a[0][i + 1] - a[0][i] for i in range(len(a[0]) - 1)])
    * max([a[1][i + 1] - a[1][i] for i in range(len(a[1]) - 1)])
)

```
# 풀이
손 가는 대로 풀었다. 리스트의 각 인접 항목별 차를 구하는 경우가 종종 있는데 
```python
[j-i for i, j in zip(t[:-1], t[1:])]
```
이렇게 하면 된다.