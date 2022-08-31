---
cdate: "2022-08-30T11:04:07"
vdate: 
  - "2022-08-30T11:04:07" # Created

isFail: false
ddate: 2022-08-30
boj_link: https://www.acmicpc.net/problem/2902
solve_times:
  - ["2022-08-30T11:04", "2022-08-30T11:13"]
---

# 2902

## 소요시간

## 문제 독해

사람 성이 들어간 알고리즘은 긴 형태와 짧은 형태 두 가지로 나뉜다.
긴 형태로만 기록해왔는데, 앞으로는 짧은 형태로 기록하려고 한다.
긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하라.

입력은 `Knuth-Morris-Pratt` 출력은 `KMP`

## 알고리즘

- 첫 번째 문자를 넣는다
- `-`가 나올때까지 찾고, 나오면 바로 뒤의 문자를 넣는다.

## 소스코드

```cpp
#include <iostream>
#include <string>

using namespace std;

string makeShort (string);

int main (void) {
    string long_form;
    cin >> long_form;

    string short_form = makeShort(long_form);
    cout << short_form << endl;

    return 0;
}

string makeShort (string long_form) {
    string short_form;
    short_form.push_back(long_form[0]);

    for (int i = 1; i < long_form.size(); i++) {
        if (long_form[i] == '-') {
            short_form.push_back(long_form[i + 1]);
        }
    }
    return short_form;
}

```

# Reference

## 참고한 것

## 더 하고싶은 것

- C++에서 문자열 스플릿, 조인 함수가 있었나. 너무 쉬워서 생각 안하고 푼 것 같다.


