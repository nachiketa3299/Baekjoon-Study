# 시간
- 30분 (실패)

# 풀이
- bfs 로 풀되 물고기를 잡아 먹을 경우 queue 를 초기화하여 새롭게 제일 가까운 물고기를 찾도록 하려했다.

# 코드

```python
N = int(input())


def bfs(ix, iy):
    global graph
    cnt = 0
    size = 2
    
    queue = [(ix, iy)]
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        cnt += 1 
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < N and 0 <= ny < N and size >= graph[ny][nx]:
                if size > graph[ny][nx] and graph[ny][nx] > 0:
                    graph[ny][nx] = 0
                    size += 1
                    queue = [(nx, ny)]
                    break
                queue.append((nx, ny))
                print(queue)


graph = []
for _ in range(N):
    print(_)
    l = list(map(int, input().split()))
    graph.append(l)
    if 9 in l:
        x = l.index(9)
        y = _
        graph[y][x] = 0
bfs(x, y)


```