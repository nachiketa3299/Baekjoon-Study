# 시간 
- 37분

# 풀이
- bfs 와 dfs 를 사용했다.
- 리스트를 print 할 때 ```" ".join(arr)``` 말고도 ```print(*arr)``` 가 있다.
- bfs 는 재귀가 아니라서 visited 같은 변수는 bfs 내부에서 생성해도 된다.


# 코드
```python
n, m, v = map(int, input().split())

# 정점이 1부터 시작이라 0번째에 가상의 정점을 추가했다.
graph = [[] for _ in range(n + 1)]

for _ in range(0, m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(0, n + 1):
    graph[i].sort()

# 정점이 1부터 시작이라 0번째에 가상의 정점을 추가했다.
visited = [False] * (n + 1)
visited_2 = [False] * (n + 1)

def dfs(start):
    global visited
    if not visited[start]:
        visited[start] = True
        print(start, end=" ")
        for node in graph[start]:
            dfs(node)

def bfs(start):
    global visited_2
    my_queue = [start]
    while len(my_queue) > 0:
        target = my_queue.pop(0)
        if visited_2[target]:
            continue
        visited_2[target] = True
        print(target, end=" ")
        for node in graph[target]:
            my_queue.append(node)


dfs(v)
print()
bfs(v)

```