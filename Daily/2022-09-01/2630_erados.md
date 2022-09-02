# 시간
- 20분 (의미없음. 다른 사람 풀이 보고 풂)

# 풀이
아주 재귀적으로 잘 짜인 코드같다.
board 만들때
```python
board = [list(map(int,input().split())) for _ in range(N)]
```
이거 잘 써먹어야겠다.
# 코드

```python
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
score = [0, 0]
def check(ix, iy, N):
    color = board[iy][ix]
    for x in range(ix, ix + N):
        for y in range(iy, iy + N):
            if color != board[y][x]:
                check(ix         , iy         , N // 2)
                check(ix + N // 2, iy         , N // 2)
                check(ix         , iy + N // 2, N // 2)
                check(ix + N // 2, iy + N // 2, N // 2)
                return
    score[color] += 1
check(0,0,N)
print(score[0])
print(score[1])
```