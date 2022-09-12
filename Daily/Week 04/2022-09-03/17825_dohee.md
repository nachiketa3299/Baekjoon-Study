# 2022-09-03

# 백준 17825 주사위윷놀이

# 63분 - 유형 simulation (BackTracking)

# 코드 - Python

```python
# 1시간 3분
from collections import defaultdict,deque
global go,score,dice,ans

ans = 0
go = [[1], [2],[3],[4],[5],[6,26],[7],[8],[9],[10],[11,21],[12],[13],[14],[15],[16,29],[17],[18],[19],[20],[-1],[22],[23],[24],[25],[20],[27],[28],[23],[30],[31],[23] ]
score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,22,24,25,30,35,13,16,19,28,27,26]

mal = [0]*4
dice = [*map(int,input().split())]

def bt(idx, nscore):
    global go, score, dice, ans
    if idx == 10: ans = max(ans,nscore); return

    kan = dice[idx]
    for m in range(4):
        if mal[m] == -1: continue
        pos = mal[m]

        if len( go[pos] ) == 2:  pos = go[pos][1]
        else:  pos = go[pos][0]
        if pos>-1:
            for _ in range(kan-1) :
                pos = go[pos][0]
                if pos == -1: break
        if pos>-1 and pos in mal: continue
        else:
            pre = mal[m]
            mal[m] = pos
            if pos == -1: bt(idx+1,nscore)
            else:bt(idx+1,nscore+score[pos])
            mal[m] = pre
bt(0,0)
print(ans)

```

# 풀이

BackTracking으로 index가 10이 될때까지 움직일 수 있는 말들을 모두 가봅니다. (말이 갈 수 있는 경우 다 가봄.)
회차마다 모든 말을 움지여보며 말이 갈 수 있는 경우(이번 회차의 움직이는 칸수만큼 갔을때 해당 칸에 이미 말이 존재할때 제외합니다.)를 모두 탐색합니다.
말을 해당 회차의 움직이는 칸수 만큼 움직였을 때, 도착지점이 아니면 점수를 더해줍니다.
마지막 회차가 끝나면 지금까지 더해진 점수와 지금까지의 최고점과 비교해서 둘 중 최댓값을 저장해줍니다.
