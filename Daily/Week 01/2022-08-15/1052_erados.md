# 풀이 시간
- 31분 30초

# 소스 코드
```python
n, k = [int(x) for x in input().split()]
additional_bottle = 0

while True:
    n_bin_rev = list(reversed([c for c in bin(n + additional_bottle)[2:]]))
    count_1 = len(list(filter(lambda x: x == "1", n_bin_rev)))

    if count_1 <= k:
        break

    additional_bottle = additional_bottle + (1 << n_bin_rev.index("1"))

print(additional_bottle)
```


# 풀이

이진수를 사용해서 물병 수를 최소로 만든 뒤 물병을 더 구매해야하면 가장 마지막에 있는 1 의 위치에 해당하는 십진수 만큼 물병을 추가했다.