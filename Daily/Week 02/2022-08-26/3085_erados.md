# 시간
- 1시간 (실패)

# 풀이
- 최고값 구하는 함수와 board 위의 두 지점을 바꾸며 최고값 구하는 함수를 호출하면 될 것 같았다.
- 뭔가 놓친 부분이 있어서 실패했다.

# 코드
```python
n = int(input())

board = [[c for c in input()] for _ in range(n)]

def calculate_maximum_count():
    temp = []
    
    # 가로로 계산
    cnt = 1
    for i in range(0, n):
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                temp.append(cnt)
                cnt = 1
    # 세로로 계산
    cnt = 1
    for i in range(0, n):
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                temp.append(cnt)
                cnt = 1
    print(temp)
    return max(temp)

def main():
    ans = 0
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                if board[i][j] != board[i][j+1]:
                    board[i][j], board[i][j+1] =  board[i][j+1], board[i][j]
                    print(board)
                    ans = max(calculate_maximum_count(), ans)
                    board[i][j], board[i][j+1] =  board[i][j+1], board[i][j]
            if i + 1 < n:
                if board[i][j] != board[i+1][j]:
                    board[i][j], board[i+1][j] =  board[i+1][j], board[i][j]
                    ans = max(calculate_maximum_count(), ans)
                    board[i][j], board[i+1][j] =  board[i+1][j], board[i][j]


    print(ans)

main()
```
