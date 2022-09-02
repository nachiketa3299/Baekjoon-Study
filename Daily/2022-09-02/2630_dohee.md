# 2022-09-02

# 백준 10844 쉬운계단수

# ? 분 - 유형 DP

# 코드 - 파이썬

```python
n = int(input().rstrip())
ans, mult = 0, 1000000000
memo = [[0]*10 for _ in range(100)]

for i in range(1,10): memo[0][i] = 1
for i in range(1,n):
    for j in range(0,10):
        if j == 0 : memo[i][j] = memo[i-1][j+1] % mult
        elif j == 9 : memo[i][j] = memo[i-1][j-1] % mult
        else : memo[i][j] = (memo[i-1][j-1] % mult + memo[i-1][j+1] % mult ) % mult

for i in range(10) :
    ans += memo[n-1][i]
    ans %= mult
print(ans)
```

# 풀이

DP 유형
옛날에 풀어봤지만 다시 풀어보니 틀렸네요.
memo[a][b]는 a는 자리수, b는 끝에서 두번째 자리에 오는 숫자로 설정해 점화식을 세워볼 수 있습니다.
0은 계단수가 1개, 9도 계단수가 1개이고 나머지수는 계단수가 2개 입니다. 0100같은 숫자가 없다는 것에 유의해야합니다.
