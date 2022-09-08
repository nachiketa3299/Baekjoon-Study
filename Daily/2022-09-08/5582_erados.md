# 시간
 - 26 분(실패)

# 풀이
길이가 긴 문자열을 움직여가며 길이가 짧은 문자열과 비교하여 점수를 구하고 그 점수중 최고점을 게속해서 기록한다.

# 코드
```python
import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

SHORT = A if len(A) < len(B) else B
LONG = B if len(A) < len(B) else A

min_len = min(len(A), len(B))
score = [0] * min_len
for offset in range(len(SHORT)-len(LONG), len(LONG)):
    temp_score = [0] * min_len
    for i in range(0, min_len):
        if 0 <= i + offset < len(LONG):
            if SHORT[i] == LONG[i + offset]:
                temp_score[i] = 1 if i == 0 else temp_score[i - 1] + 1
                score[i] = max(temp_score[i], score[i])
print(max(score))
```