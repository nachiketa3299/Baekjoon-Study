# 시간
- 14분

# 풀이
- 사람 정보를 받으면서 이때까지 받은 사람 정보와 비교하여 rank 를 늘렸다.

# 코드

```python
n = int(input())

rank = [1] * n
dungch = []

# 한 사람씩 입력받으면서
for i in range(n):
    dungch.append(list(map(int, input().split())))
    # 이때까지 입력받은 사람과 비교하여
    for j in range(i):
        # 자기가 덩치크면 다른사람 랭크를 낮추고
        if dungch[i][0] > dungch[j][0] and dungch[i][1] > dungch[j][1]:
            rank[j] += 1
        # 남이 덩치크면 자기 랭크를 낮춘다.
        elif dungch[i][0] < dungch[j][0] and dungch[i][1] < dungch[j][1]:
            rank[i] += 1

print(" ".join(map(str,rank)))

```
