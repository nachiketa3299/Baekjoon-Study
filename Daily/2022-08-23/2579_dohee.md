---
날짜: "2022-08-23"
문제번호:
  - "2579"
  - "1620"
---

# 2022-08-23

# 28분 - 유형 DP

# 코드

```python
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
```

#풀이
DP 로 해결
dp[floor] 에 해당 계단까지 올라왔을때, 해당 계단을 밟는 최대한의 점수 저장
(1)지금 층과 바로 한칸 아래층 밟는 경우
(2)지금 층과 두칸 아래층 밟는 경우
두가지 경우를 비교해서 더 큰 값을 저장해나가면 됨
