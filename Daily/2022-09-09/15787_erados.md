# 시간
- 27 분

# 풀이
- 비트마스킹 문제인데 비트마스킹으로 못 풀었다.

# 코드
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [['0']*20 for _ in range(N)]
for i in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        arr[command[1] - 1][command[2] - 1] = '1'
    elif command[0] == 2:
        arr[command[1] - 1][command[2] - 1] = '0'
    elif command[0] == 3:
        arr[command[1] - 1].pop()
        arr[command[1] - 1].insert(0,'0')
    else:
        arr[command[1] - 1].pop(0)
        arr[command[1] - 1].append('0')
    
print(len(set(list(map(''.join, arr)))))
```