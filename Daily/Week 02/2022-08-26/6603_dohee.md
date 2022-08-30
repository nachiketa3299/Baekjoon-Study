# 2022-08-25

# 백준 6603 로또

# 20분 - 유형 BackTracking

# 코드 - Python

```python
global k,n
l = []
k, n = 0, 0
def BT(cur, arr, start):
    if cur == 6: print(*arr)
    elif cur<k and start<n :
        for i in range(start, n):
            tmp = arr[cur]
            arr[cur] = l[i]
            BT(cur+1, arr, i+1)
            arr[cur] = tmp

while True:
    st = input().rstrip()
    if st == "0": break
    l = list( map(int, st.split()) )
    k = l[0]


    del l[0]
    l.sort()
    n = len(l)
    arr = [0]*6

    BT(0, arr, 0)
    print()


```

# 풀이

처음부터 입력받은 수들을 오름차순 정렬해준다.
BT로 recursive하게 하나씩 선택하도록 로직을 짰다.
6개를 선택했다면 출력이 이루어지고, 지금보다 후에 선택할때 더 작은 숫자가 나오지 않도록 for 문을 변형했다.
