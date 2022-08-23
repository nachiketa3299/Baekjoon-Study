---
날짜: "2022-08-23"
문제번호:
  - "2579"
  - "1620"
---

# 2022-08-23

# 28분 - 유형 DP

n = int(input().rstrip())
arr = [0]*n
dp = [0]*n
for i in range(n) : arr[i] = int(input().rstrip())
if n <= 2: print(sum(arr)); exit(0)

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max( arr[0]+arr[2], arr[1]+arr[2] )

for i in range(3,n): dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i] )

print(dp[n-1])
