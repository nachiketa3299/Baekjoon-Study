# 시간
- 37분

# 풀이
- 그래프를 순환하면서 1이 보이면 bfs 로 근처의 1을 0으로 만들어버리면 된다.

# 코드

```python
import sys
input = sys.stdin.readline


def bfs(ix, iy):
    queue = [(ix, iy)]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        for move in moves:
            dx, dy = move
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if land[ny][nx] == 1:
                    land[ny][nx] = 0
                    queue.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0

    land = [[0 for _ in range(N)] for _ in range(M)]
    for __ in range(K):
        y, x = map(int, input().split())
        land[y][x] = 1

    
    for x in range(N):
        for y in range(M):
            if land[y][x] == 1:
                land[y][x] = 0
                bfs(x, y)
                cnt += 1

    print(cnt)

```