# 시간
- 30분

# 풀이
- n 번째 계단을 밟으려면 n-2 를 밟고 n 을 밟거나 n-3, n-1 을 밟고 n 을 밟아야한다. 그 중 가장 큰 점수를 n 번째 계단을 밟았을 때의 최고 점수로 저장하고 계단을 밟아나가면 된다.

# 코드

```python
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    score_by_stair = []
    dp = []

    # 계단별 점수 저장
    for i in range(0, n):
        score_by_stair.append(int(input()))

    dp.append(score_by_stair[0])

    # IndexError 방지
    if n == 1:
        print(dp[0])
        return

    dp.append(score_by_stair[0] + score_by_stair[1])

    # IndexError 방지
    if n == 2:
        print(dp[1])
        return

    dp.append(max(score_by_stair[0] + score_by_stair[2] , score_by_stair[1] + score_by_stair[2]))

    for i in range(3, n):
        dp.append(max(dp[i - 2] + score_by_stair[i], dp[i - 3] + score_by_stair[i - 1] + score_by_stair[i]))

    print(dp[n - 1])


main()
```
