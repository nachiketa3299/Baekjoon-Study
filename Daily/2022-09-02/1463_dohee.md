# 2022-09-02

# 백준 1463 1로만들기

# 25분 - 유형 DP

# 코드 - Python

```python
from collections import defaultdict, deque
INF = 1000001
n = int(input().rstrip())
memo = [INF]*(n+1)
memo[1] = 0
if n <= 1 : print(0); exit(0)
if n == 2 : print(1); exit(0)
memo[2] = 1
memo[3] = 1
for i in range(4,n+1):
    if i/2%1 == 0: memo[i] = memo[i//2]+1
    else : memo[i] = memo[(i-1)//2]+2
    if i/3%1 == 0: memo[i] = min( memo[i], memo[i//3]+1 )
    elif (i-1)/3%1 == 0: memo[i] = min( memo[i], memo[(i-1)//3]+2 )
    memo[i] = min(memo[i-1]+1, memo[i])

print(memo[n])

```

# 풀이

memo[a] 는 a를 1로 만들기 위해 필요한 최소 계산의 수를 저장합니다.
숫자 n이전의 값은 모두 알고있다는 가정하에
수리적으로 memo[n]의 값은 다음중 무조건 하나일 수 밖에 없습니다.
(1) n-1의 최소계산 횟수 + 1
(2) n이 2의 배수일때, n//2의 최소계산 횟수 + 1
(3) n이 3의 배수일때, n//3의 최소계산 횟수 + 1
