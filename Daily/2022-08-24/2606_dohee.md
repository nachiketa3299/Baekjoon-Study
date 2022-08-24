# 2022-08-24

# 15분 - 유형 BFS

# 코드

```python
from collections import defaultdict,deque
n = int(input().rstrip())
e = int(input().rstrip())
dic = defaultdict(int)
for ee in range(e):
    a,b = map(int, input().split())
    a, b = a-1,b-1
    dic[(1<<a)] |= (1<<b); dic[ (1<<b) ] |= (1<<a)
q = deque()
ans = 0
q.append((1<<0))
visit = (1<<0)
while q:
    now = q.popleft()
    nodebit = dic[now]
    while nodebit:
        nextt = nodebit & -nodebit
        nodebit &= (nodebit-1)
        if visit & nextt: continue
        visit |= nextt
        ans += 1
        q.append(nextt)
print(ans)
```

#풀이
비트마스킹을 활용
