# 2022-08-29

# 백준 23288 주사위 굴리기 2

# 1시간 45분 - 유형 Simulation and DFS(BFS)

# 코드 - Python

```python
from collections import defaultdict, deque
global n,m,k,now_d, sy,sx,ans, cnt
visit = []; arr=[]
now_d, sy,sx,ans, cnt = 0,0,0,0, 0
n,m,k = map(int,input().split())
g = [[*map(int,input().split())] for _ in range(n)]
dic = defaultdict(int)
dic[0] = 1; dic[1] = 0; dic[2] = 3; dic[3] = 2
clock = defaultdict(int)
clock[0] = 3; clock[3] = 1; clock[1] = 2; clock[2] = 0 # 시계방향으로 90도 회전하면 어느 방향이 되는지 해시
anti = defaultdict(int)
anti[0] = 2; anti[2] = 1; anti[1] = 3; anti[3] = 0     # 반시계방향으로 90도 회전하면 어느 방향이 되는지 해시

dir = [(0,1), (0,-1), (-1,0), (1,0) ] #  동 서 북 남
dice = [1,2,3,4,5,6] # 바닥면이 index 5에 저장됨

rev = [[2,1,5,0,4,3], [3,1,0,5,4,2],[1,5,2,3,0,4], [4,0,2,3,5,1] ]
y,x = sy, sx

score = [[0]*m for _ in range(n)]

def dfs(y,x, num):
    global n, m, k, now_d, sy, sx, ans, cnt
    for d in dir:
        ny,nx = y+d[0], x+d[1]
        if ny<0 or nx<0 or ny>=n or nx>=m:continue
        if visit[ny][nx] or g[ny][nx]!=num: continue
        arr.append((ny,nx))
        visit[ny][nx] = True
        dfs(ny,nx,num)
    return


for kk in range(k):
    # 1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    ny,nx = y+dir[now_d][0], x+dir[now_d][1] # 1번 주사위 이동방향으로 한칸 굴려보기

    if ny<0 or nx<0 or ny>=n or nx>=m: # 이동방향에 칸이 없을때
        now_d = dic[now_d]             # 이동방향에 칸이 없어서 이동방향을 반대로 해줌
        ny, nx = y + dir[now_d][0], x + dir[now_d][1]  # 바뀐 이동방향에 따라 한칸 이동
    y, x = ny, nx


    # 주사위 굴려주기
    d2 = dice.copy()
    for i in range(6) : dice[ rev[now_d][i] ] = d2[i]


    # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득
    if score[ny][nx] == 0 : # 점수를 모름으로 찾아줘야한다. ( 지도는 자연수로 이루어져서 점수는 0이 나올 수 없다. 그러므로 점수를 아직 안찾은 상태를 0으로 표기.  점수는 고정되어있으므로 한번 찾아준 점수는 저장해둔다. )
        visit = [[False] * m for _ in range(n)]
        visit[ny][nx] = True
        arr = [(ny,nx)]
        dfs(ny, nx, g[ny][nx]) # dfs 를 하며 동서남북으로 이동할 수 있으면서, 칸의 값이 동일한 경우의 좌표를 모두 arr에 저장한다.
        cnt = len(arr)
        for l in arr : yy,xx = l; score[yy][xx] = cnt*g[ny][nx] # arr의 모든 좌표들은 점수가 동일하므로, 점수를 알게된 김에 미리 다 저장해준다.

    ans += score[ny][nx] # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득



    # 3 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정
    if dice[5] > g[ny][nx] : now_d = clock[now_d]   #  이동 방향을 90도 시계 방향으로 회전
    elif dice[5] < g[ny][nx] : now_d = anti[now_d]  #  이동 방향을 90도 반시계 방향으로 회전

print(ans)

```

# 풀이

(1) 이동 방향에 따라 그 다음 좌표( ny, nx )를 알아냄
-> 이동 가능한 좌표이면 이동
-> 이동 불가능한 좌표이면, 방향을 반대로 해주고, 바뀐 방향에 따라 다시 그 다음 좌표를 구해줌

(2) 주사위 굴려주기

(3) 주사위가 도착 예정인 칸( ny,nx )의 점수를 획득
( 특정 위치의 점수값은 불변하기에 dfs나 bfs로 점수를 계산해서 저장해두면 시간초과를 면할 수 있음 )
-> 점수를 구하지 않은 상태면 BFS/DFS로 점수 계산해서 저장

(4)
주사위 바닥면 값 > 칸의 값 : 이동방향을 90도 회전
주사위 바닥면 값 < 칸의 값 : 이동방향을 90도 반시계 방향으로 회전
