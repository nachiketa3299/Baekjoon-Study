# 풀이 시간
- 23:06 ~ 00:53 107분
- 기타 시간 51분
- 총 158분

# 소스 코드

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool hasTwoConsOne (vector<int> arr) {
    for (int i = 1; i < arr.size() - 1;) {
        if (arr[i] == 1) {
            if (arr[i + 1] == 1) {
                return true;
            } else if (arr[i + 1] != 1) {
                i += 1;
            }
        } else {
            i += 1;
        }
    }
    return false;
}

vector<vector<int>> possibleSum (const int size) {
    vector<vector<int>> pos_sums;
    int max_twonum = size / 2;
    for (int twonum = 0; twonum < max_twonum + 1; twonum++) {
        int onenum = size - 2 * twonum;
        int cur_size = onenum + twonum;
        vector<int> sub (onenum, 1);
        sub.resize(cur_size, 2);
        do {
            if (!hasTwoConsOne(sub)) {
                pos_sums.push_back(sub);
            }
        } while (next_permutation(sub.begin(), sub.end()));
    }
    return pos_sums;
}

vector<int> calScore (vector<vector<int>> pos_sum, vector<int> step_s) {
    vector<int> scores;
    for (int i = 0; i < pos_sum.size();i++) {
        int sum = 0;
        int index = 0;

        for (auto e: pos_sum[i]) {
            cout << e << " ";
        }
        cout << endl;

        for (int j = 0; j < pos_sum[i].size(); j++) {
            index += pos_sum[i][j];
            sum += step_s[index - 1];
            cout << "- tosumi: " << index - 1 << ", - tosum:" << step_s[index - 1] << endl;
        }
        cout << "- sum: " << sum << endl;
        scores.push_back(sum);
    }
    return scores;
}

int main (void) {
    int STEP_SIZE;
    cin >> STEP_SIZE;

    // Initialize scores of each step
    vector<int> step_scores(STEP_SIZE);
    for (auto &e: step_scores) {
        cin >> e;
    }
    // step_score 에 계단별 점수가 저장된다.

    vector<vector<int>> possible_sums = possibleSum(STEP_SIZE);
    for (auto e: possible_sums) {
        for (auto s: e) {
            cout << s << " ";
        }
        cout << endl;
    }
    vector<int> possible_scores = calScore(possible_sums, step_scores);

    cout << *max_element(possible_scores.begin(), possible_scores.end()) << endl;
    return 0;
}
```

# 알고리즘

- 계단의 갯수를 `N`이라고 할 때 1과 2의 합으로 `N`을 나타내는 가짓수를 구하되, 다음의 규칙을 지켜야 한다.
    - 1이 2번 연속해서 나오면 안된다. 단, 첫 2회는 괜찮다.
- 위 규칙을 만족하도록 구한 모든 *패턴*들에 대해서 점수를 계산하고, 그 중에서 최댓값을 구하면 되었다.

# 어려웠던 것

- 순열을 사용하는 것 외에 다른 방법이 없는지 많이 고민했는데, 생각이 나질 않아서 (정확히는 패턴의 갯수는 쉽게 구할 수 있으나, 패턴 자체는 구하기가 어려웠다.) 그냥 순열을 사용하기로 했다.
- 정답이 제대로 나옴에도 불구하고, 시간 초과가 났다. **패턴을 구하는 것에 내가 모르는 다른 방법이 있나?** 심지어 표준에 있는 순열 함수를 가져다 썼는데.

# 더 알아볼것 & 참조 링크 

- C++ Vector 관련
    - [C++ Vector 최대값, 최소값, 인덱스 구하기/Notepad](https://notepad96.tistory.com/40)
- C++ 함수의 인자화에 대해서
    - [C++에서 함수를 인자로 전달하는 방법/내이름은 다빈](https://mynameisdabin.tistory.com/17)
- C++ `size_`형에 대해서
    - [C언어\] `size_t`형의 의미; `unsigned int`와 차이점, 차이/mwultong Blog ... 프로그래밍/계산기](http://mwultong.blogspot.com/2007/06/c-sizet-unsigned-int.html)
- C++ 순열
    - [How to create a permutation in c++ using STL for number of places lower than the total length/stackoverflow](https://stackoverflow.com/questions/61392431/how-to-create-a-permutation-in-c-using-stl-for-number-of-places-lower-than-the)
    - [\[C++/Algorithm\] 순열(next_permutation) 사용 방법과 조합(Combination) 구하기/mjmjmj98](https://mjmjmj98.tistory.com/38)
    - [C++ 순열, 조합 알고리즘(`next_permutation`)/Reco.dy](https://velog.io/@ddyy094/C-순열조합-알고리즘nextpermutation)