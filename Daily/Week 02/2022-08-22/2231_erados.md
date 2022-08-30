# 시간
- 19분

# 풀이
- 어떤 수 A 의 생성자는 A 에서 A의 자릿수 * 9 를 뺀 것보단 커야하므로 시작점을 A - A의 자릿수 * 9 로 하고 brute force 로 풀었다.

# 소스
```python
# 분해합을 반환
def BHH(n):
    return n + sum([int(i) for i in str(n)])

a = int(input())

# 어떤 수 A 의 생성자는 A 에서 A의 자릿수 * 9 를 뺀 것보단 커야한다.
test_number = a - len(str(a)) * 9
if test_number < 0:
    test_number = 0

def main():
    global test_number
    while True:
        if BHH(test_number) == a:
            print(test_number)
            break;
        
        elif test_number == a:
            print(0)
            break

        test_number += 1

main()
```
