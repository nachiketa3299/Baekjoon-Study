from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
coms = []
for _ in range(M):
    coms.append(list(map(int, input().split())))

trains = [deque([0]*20) for _ in range(N)]
for com in coms:
    if com[0] == 1:
        k, i, x = com
        trains[i-1][x-1] = 1
    if com[0] == 2:
        k, i, x = com
        trains[i-1][x-1] = 0
    if com[0] == 3:
        k, i = com
        trains[i-1].pop()
        trains[i-1].appendleft(0)
    if com[0] == 4:
        k, i = com
        trains[i-1].popleft()
        trains[i-1].append(0)

ans = 0
check = []
for train in trains:
    if train in check:
        continue
    check.append(train)
    ans += 1
print(ans)