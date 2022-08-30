# 시간
- 42분

# 풀이
- sys.stin.readline 이 핵심이다.......
dictionary 넣을 때 

```python
dict(zip(list, range(1,m+1)))
```

이렇게 할 수 있다.

# 코드

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dogam_list = []
dogam_dict = {}


# 똥같은 코드..
for i in range(1, n + 1):
    name = input().rstrip()
    dogam_list.append(name)
    dogam_dict[name] = str(i)

# print 여기서 하면 input 이랑 꼬인다.
for i in range(1, m + 1):
    q = input().rstrip()
    print(dogam_list[int(q) - 1] if q.isdigit() else dogam_dict[q])

```