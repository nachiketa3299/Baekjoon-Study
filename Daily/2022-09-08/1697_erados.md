# 시간
 - 34분 (시간초과)

# 풀이
 - bfs 에서 단계를 구할 필요가 있을때 queue 에 저렇게 넣거나 따로 배열을 만들어서 index 로 접근하면 된다.

# 코드
```python
import sys
input = sys.stdin.readline

S, D = map(int, input().split())

my_queue = [(S, 0)]
visited = [0] * 200002

if S-D > 0:
    print(S-D)
    exit(0)

while len(my_queue) > 0:
    target, time = my_queue.pop(0)
    visited[target] = 1
    if target == D:
        print(time)
        break
    if target <= 100000:
        new_time = time + 1
        if target > 0 and not visited[target-1]:
            my_queue.append((target-1, new_time))
        if not visited[target+1]:
            my_queue.append((target+1, new_time))
        if not visited[target*2]:
            my_queue.append((target*2, new_time))
    
```