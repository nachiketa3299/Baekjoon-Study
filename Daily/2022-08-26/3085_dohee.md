# 2022-08-25

# 백준 1260 DFS와BFS

# 15분 - 유형 DFS, BFS

# 코드 - 파이썬

```python
from collections import defaultdict, deque

ndic = defaultdict(int)
b_num = defaultdict(int)

n, m, v = map(int, input().split())

for _ in range(m):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    ndic[ (1<<a) ] |= (1<<b)
    ndic[ (1<<b) ] |= (1<<a)
    b_num[ (1<<a) ] = a
    b_num[ (1<<b) ] = b

visit = (1<<(v-1))
def dfs( now ) :
    global visit
    print(b_num[now]+1, end=" ")
    nodegroup = ndic[now]
    while nodegroup :
        nextt = nodegroup&-nodegroup
        nodegroup &= (nodegroup-1)
        if nextt & visit: continue
        visit |= nextt
        dfs(nextt )

def bfs(v):
    q = deque([(1<<v)]); visit = (1<<v)
    while q:
        now = q.popleft()
        print(b_num[now]+1, end=" ")
        nodegroup = ndic[now]
        while nodegroup:
            nextt = nodegroup&-nodegroup
            nodegroup &= (nodegroup-1)
            if visit & nextt: continue
            visit |= nextt
            q.append(nextt)

dfs(1<< (v-1) )
print()
bfs(v-1)
```

#풀이
비트마스킹을 활용
저장시 노드 번호를 0부터 시작하도록 작성
메모리를 많이 이용하므로 노드 개수가 매우 많을때는 추천하지 않는 방법

###ndic (해시)

ndiv[ ( 1 << 노드번호) ] = 연결된 다른 모든 노드의 비트

###b_num (해시)

b_num[ (1<<노드번호) ] = 노드번호

###알고리즘 자체는 기본적인 dfs와 bfs 알고리즘을 그대로 활용
