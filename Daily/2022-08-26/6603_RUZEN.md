---
tags:
aliases:
cdate: "2022-08-26T16:43:50"
vdate: 
  - "2022-08-26T16:43:50" # Created
boj_link: https://www.acmicpc.net/problem/6603
solve_times:
---

# 6603

66분

## 풀이 시간

## 문제 독해

- 독일 로또는 1부너 49까지의 숫자 중에서 총 6개의 수를 고른다.
- 로또 번호를 선택하는 가장 유명한 전략은 49가지 수 중 $k$ $(k>6)$ 개의 수를 골라 집합 $S$를 만든 다음, 그 집합 내의 수에서만 번호를 선택하는 것이다.
- 집합 $S$와 $k$가 주어졌을 때, **로또에 사용될 수 6개를 고르는 모든 방법을 구하라**.

문제를 읽자마자 든 생각은 조합(Combination) 구현 문제라는 것.
순열 문제를 언젠가 풀었던 것 같은데, 그것의 연장선상에 있는 것 같다.

- 입력은 여러 개의 테스트 케이스이다.
    - 각 테스트 케이스는 한 줄로 이루어져 있다.
    - 한 테스트 케이스의 첫 번째 수는 $k (6 < k < 13)$이고, 다음엔 $k$개$(k \in S)$ 의 숫자가 온다.
    - $S$의 원소는, 오름차순으로 주어진다.
    - 입력의 마지막 줄에는 $0$이 하나 주어진다.
- 출력은 각 테스트 케이스마다 수를 고르는 모든 방법을 출력하는 것이다. 
- 이 때, 사전 순으로 출력한다.
- 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

## 입출력 예제

```sh
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
```

```sh
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
```

## 풀이
- 입력부 구현:
    - 우선 `0`을 입력받을 때까지 테스트 케이스를 받아오는 것을 구현해야 할 것 같다.
- 그리고 테스트 케이스를 저장할 `vector<vector<int>> T`를 선언한다.
- `T[i]` 마다 반복문을 돌며 다음을 실행한다.
    - `Combi(T[i])` 의 결과로 `vector<vector<int>>` 형으로 한 테스트케이스의 모든 경우의 수가 만들어진다. 이걸 `vector<vector<vector<int>>> R (T.size())` 에 푸시한다.

그리고, 문제 풀이의 핵심인 `vector<vector<int>> Combi(vector<int> pattern)` 를 구현한다.

## 소스 코드

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#define PICK 6

using namespace std;


vector<vector<int>> Combination (vector<int>, int); 
void printVec(vector<vector<int>>);

bool cmp(vector <int> a, vector <int> b) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] == b[i]) {
            continue;
        } else {
            return (a[i] > b[i]);
        }
    }
}

int main (void) {

    vector<vector<int>> Testcases;
    int k;

    do {
        cin >> k;
        vector<int> temp_vec;
        for (int i = 0; i < k; i++) {
            int temp;
            cin >> temp;
            temp_vec.push_back(temp);
        }
        if (k != 0) {
            Testcases.push_back(temp_vec);
            temp_vec.resize(0);
        }
    } while (k != 0);


    for (vector<int> &testcase: Testcases) {
        vector<vector<int>> Result = Combination(testcase, PICK);
        printVec(Result);
    }

    return 0;
}

vector<vector<int>> Combination (vector<int> testcase, int r) {
    vector<vector<int>> result;
    int n = testcase.size();

    vector<bool> mask (n - r, false);
    mask.insert(mask.end(), r, true);
    // ex if n = 8, r = 6
    // mask = {false, false, true, true, true, true}

    do {
        vector<int> temp (0);
        for (int k = 0; k < n; k++) {
            if (mask[k] == true) {
                temp.push_back(testcase[k]);
            }
        }
        sort(temp.begin(), temp.end());
        result.push_back(temp);
    } while (next_permutation(mask.begin(), mask.end()));
    sort(result.begin(), result.end(), cmp);
    return result;
}


void printVec(vector<vector<int>> vec) {
    for (auto v: vec) {
        for (auto a: v) {
            cout << a << " ";
        }
        cout << endl;
    }
    cout << endl;
    return;
}

```

순서 정렬이 안 돼서 실패!!!!!!!!
거의 다 했으니 오늘 제출할 것


