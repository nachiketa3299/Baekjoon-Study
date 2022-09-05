# 2022-08-30

# 백준 2909 kmp는 왜 kmp일까?

# 3분 - 유형 문자열


# 코드 - Python

```python
ans = ""
l = list(input().split('-'))
for ll in l: ans+=ll[0]
print(ans)
```

# 풀이

파이썬의 split()내장 함수를 써서 '-'를 기준으로 슬라이싱한다.
그 결과물을 리스트로 담아
각 이름의 첫글자(각 리스트 원소의 첫 글자)만 더하여 출력한다.