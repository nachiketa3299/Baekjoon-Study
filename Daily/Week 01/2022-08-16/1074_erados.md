# 시간
- 25분 06초

# 코드
```python
N, r, c = map(int, input().split())


def c_to_num(c):
    num = 0
    for i, x in enumerate([char for char in bin(c)[2:][::-1]]):
        if x == "1":
            num += 1 << i << i

    return num


print(c_to_num(c) + c_to_num(r) * 2)
```

# 풀이
index 를 binary 로 하면 될 것 같았다.
각 열번호를 2진법으로 나타낸 뒤 4진법으로 해석하면 0 행에 해당하는 숫자가 나왔다.
0 열은 거기에 2를 곱한 것이었다.
왜 그런진 모르겠다.

```python
int(f'{c:b}', 4)  
```
쓰면 훨씬 간단하다.