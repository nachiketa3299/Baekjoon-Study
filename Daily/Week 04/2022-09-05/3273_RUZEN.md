---
tags:
aliases:
  - 스타트와 링크
cdate: "2022-09-05T12:00:43"
vdate: 
  - "2022-09-05T12:00:43" # Created

keyword:
  - Time Complexity
  - Counting
rank: S3
isFail: true
ddate: 2022-09-05
boj_link: https://www.acmicpc.net/problem/3273
solve_times:
  - [2022-09-05T13:42, 2022-09-05T14:02]
  - [2022-09-05T14:18, 2022-09-05T15:44]
  - [2022-09-05T16:29, 2022-09-05T17:06]
---

# 3273

## 소요시간

## 문제 독해

수열 $a_1, a_2, ... a_n$이 있다. 이 수열의 원소 $a_i$는 $1 \leq a_i \leq 1,000,000$을 만족한다.  
자연수 $x$가 주어진다.  
$1 \leq i < j \leq n$인 $i$, $j$에 대해서 $a_i + a_j = x$를 만족하는 $(a_i, a_j)$쌍의 수를 구하는 프로그램을 작성하라.  

`00` $n$ (수열의 크기)
`01` $a_0$⎵$a_1$ ... $a_n$
`02` $x$

## 알고리즘

첫 시도로 그냥 브루트 포스로 두 수열 원소간의 합을 저장한 2차원 벡터를 구성한 후 각 칼럼마다 $x$에 해당하는 값의 갯수를 찾아 더하려고 했다.  
답은 나왔지만 메모리 초과가 떴다. 

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (void) {
    int n;
    cin >> n;
    vector<int> sequence;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        sequence.push_back(t);
    }
    int x;
    cin >> x;

    vector<vector<int>> vec_sum (n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            vec_sum[i][j] = sequence[i] + sequence[j];
        }
    }
    int c = 0;
    for (int j = 0; j < n; j++) {
        vector<int>::iterator begin = vec_sum[j].begin();
        advance(begin, j + 1);
        c += count(begin, vec_sum[j].end(), x);
    }
    cout << c << endl;
    return 0;
}
```

다른 방법을 시도해 보았다.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (void) {
    int n;
    cin >> n;
    vector<int> sequence;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        sequence.push_back(t);
    }
    int x;
    cin >> x;
    int c = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n;j++) {
            if (sequence[i] + sequence[j] == x) {
                c++;
            }
        }
    }

    cout << c << endl;
    return 0;
}
```

비슷한 방법인데 2차원 배열을 만들지 않고 직접 더해서 판단했다.  
이번엔 시간 초과가 떴다.





## 소스코드

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (void) {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<int> sequence;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        sequence.push_back(t);
    }
    int x;
    cin >> x;
    int c = 0;

    if (x == 1) {
        ;
    } else {
        sort(sequence.begin(), sequence.end());
        int max_index = n - 1;

        while (sequence[0] + sequence[max_index] > x) {
            max_index--;
        }

        for (int j = max_index; j > 0; j--) {
            for (int i = 0; i < j; i++) {
                if (sequence[i] + sequence[j] == x) {
                    c++;
                }
            }
        }

    }


    cout << c << "\n";
    
    return 0;
}
```

수열을 일단 오름차순으로 정렬한 후 합이 $x$가 나올 수 있는 경우의 인덱스 부분에서만 `for`문을 실행했다.  
그럼에도 불구하고 복잡도가 역시 $O(n^2)$라 그런지 여전히 시간 초과가 떴다.  
문제를 풀다가 디버거가 말썽이라 요리조리 해맸기 때문에 시간은 의미가 있나 싶다.  


# Reference

## 참고한 것

- [`std::count`/cplusplus](https://cplusplus.com/reference/algorithm/count/)
- [C++ 원소 개수 구하기 `count`/Notepad](https://notepad96.tistory.com/45)
- [C++에서 Vector의 요소 개수 찾기/TECHIE DELIGHT\<\\\>](https://www.techiedelight.com/ko/find-count-of-an-element-in-a-vector-in-cpp/)
- [C++에서 Vector의 특정 위치에 대한 반복기 가져오기/TECHIE DELIGHT\<\\\>](https://www.techiedelight.com/ko/get-iterator-specific-position-vector-cpp/)

## 더 하고싶은 것

문제가 안풀려서 우울하다....

