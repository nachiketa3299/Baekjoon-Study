# 시간
재풀이
# 코드
```python
N = int(input())
board = [list(input()) for _ in range(N)]

def swap(i,j,x,y):
    temp = board[i][j]
    board[i][j] = board[x][y]
    board[x][y] = temp


def max_len():
    row_max, col_max = 0, 0
    for i in range(N):
        row_len= 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                row_len+=1
            else:
                row_len = 1
            row_max = max(row_len, row_max)

    for j in range(N):
        col_len =1
        for i in range(N-1):
            if board[i][j] == board[i+1][j]:
                col_len+=1
            else:
                col_len = 1
            col_max = max(col_len, col_max)
    return max(row_max, col_max)


m=0
for i in range(N):
    for j in range(N):
        for (dx, dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            x,y = i+dx, j+dy
            if x<0 or y<0 or x>=N or y>=N: continue
            if board[i][j] != board[x][y]:
                swap(i,j,x,y)
                l = max_len()
                m = max(m,l)
                swap(x,y,i,j)

print(m)
```
# 풀이
- 가장 기본적인 방법으로 풀이하였다. 함수를 따로 만들어 자리를 바꾸어보고, 가장 긴 길이를 찾아서 저장한다. 이 과정을 반복한다.  이 때, 길이를 찾는 함수는 행마다, 열마다 돌면서 가장 긴 길이를 찾는다. 둘 중 어느 것이든 길면 마지막 출력값이 된다.

# 기록
- 보다시피 for문을 여러번 쓰기 때문에, python3에선 시간초과위험이 있다. pypy3에서 통과한다.
