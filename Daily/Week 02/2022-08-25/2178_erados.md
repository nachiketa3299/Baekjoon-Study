# 시간
- 38분

# 풀이
- 똥같은 코드..
- 신경써야할 부분이 몇 군데 있는데
1. 문제에서 주는 index 는 1부터 시작한다.
2. 인접한 cell 로 이동할 때 대각선 이동은 불가하다.
3. 인접한 cell 로 이동할 때 IndexError 를 피해야한다.

# 코드
```python
n, m = map(int, input().split())

board = [[int(c) for c in input()] for _ in  range(n)]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    visited = [[True] + [False] * (m) for _ in range(n + 1)]
    visited[0] = [True] * (m + 1)
    my_queue = [(1,1,1)]
    while len(my_queue) > 0:
        target = my_queue.pop(0)
        if not visited[target[0]][target[1]]:
            if board[target[0]-1][target[1]-1] == 1:
                visited[target[0]][target[1]] = True
                if target[0:2] == (n, m):
                    print(target[2])
                    break
                for move in moves:
                    x = target[0] + move[0]
                    y = target[1] + move[1]
                    if x < n + 1 and y < m + 1:
                            my_queue.append((x, y, target[2]+1))

bfs()
```