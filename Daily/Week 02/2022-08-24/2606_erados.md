# 시간
- 24분

# 풀이
dfs를 사용했다. 처음에
```python
 graph = [[]] * n 
```
을 사용했었는데 _copy by reference_ 되어서 같은 배열이 중복되었다.

# 코드
```python
n = int(input())
m = int(input())
ans = 0

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, k = map(int, input().split())
    graph[i].append(k)
    graph[k].append(i)

visited = [False] * (n + 1)


def dfs(start):
    global ans
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)
            ans += 1


dfs(1)
print(ans)
```