# 시간 
- 50분 (실패)

# 풀이
- 남은 숫자의 수를 현재 고른 숫자의 수와 합쳐도 6이 안되면 넘어가는 로직을 넣으려 했는데 잘 안됐다.


# 코드

```python
n = 0
data = []
ans = []
def dfs(index):
    global n, data, ans
    if len(ans) < 6 and (n - index + 1) >= 6- len(ans):
        for i in range(index , n):    
            ans.append(data[index])
            if len(ans) == 6:
                print(" ".join(ans))
            dfs(i + 1)
            ans.pop()

    

while True:
    temp = list(map(int,input().split()))
    if temp[0] == 0:
        break
    n, data = int(temp[0]), temp[1:]
    dfs(0)
```
