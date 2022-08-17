# 풀이 시간

- `[2022-08-16T18:35, 2022-08-16T19:42]` 67분
- `[2022-08-17T10:12, 2022-08-17T10:39]` 27분
- `[2022-08-17T13:33, 2022-08-17T14:47]` 74분
- 총 **168 분**

# 소스 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<string> StringVector;

#define WIN 2
#define DRAW 1
#define LOSE 0

int verify (char sg, char oth) {
    if (sg == oth) {
        return DRAW;
    } else {
        if (sg == 'S') {
            return (oth == 'P') ? WIN : LOSE;
        } else if (sg == 'P') {
            return (oth == 'R') ? WIN : LOSE;
        } else {
            return (oth == 'S') ? WIN : LOSE;
        }
    }
}

int calScore (string sg_in, StringVector all_in) {
    int score_sum = 0;
    for (string &e_in: all_in) {
        for (int i = 0; i < sg_in.size(); i++) {
            score_sum += verify(sg_in[i], e_in[i]);
        }
    }
    return score_sum;
}

StringVector toRoundSet (StringVector input) {
    const int round_num = input.size();
    const int people_num = input[0].size();

    StringVector per_round_set;
    per_round_set.resize(people_num);
    for (int p = 0; p < people_num; p++) {
        per_round_set[p].resize(round_num);
    }

    for (int p = 0; p < people_num; p++) {
        for (int r = 0; r < round_num; r++) {
            per_round_set[p][r] = input[r][p];
        }
    }

    return per_round_set;
}

vector<int> allPossibleScore (string round_set) {
    vector<int> score_arr_per_RSP = { 0, 0, 0 };
    
    for (int p = 0; p < round_set.size(); p++) {
        // Case if SG is 'R'
        score_arr_per_RSP[0] += verify('R', round_set[p]);
        // Case if SG is 'S'
        score_arr_per_RSP[1] += verify('S', round_set[p]);
        // Case if SG is 'P'
        score_arr_per_RSP[2] += verify('P', round_set[p]);
    }
    return score_arr_per_RSP;
}

int calMaxScore (StringVector all_in) {
    int max_score_sum = 0;
    const int round_num = all_in.size();
    const int people_num = all_in[0].size();

    StringVector per_round_set = toRoundSet(all_in);

    for (int p = 0; p < people_num; p++) {
        vector<int> possible_score_arr = allPossibleScore(per_round_set[p]);
        max_score_sum += *max_element(possible_score_arr.begin(), possible_score_arr.end());
    }

    return max_score_sum;
}

int main (void) {
    int R, N;
    string sangeunInput;
    StringVector otherInputs;

    cin >> R;
    sangeunInput.resize(R);
    for (string &s: otherInputs) {
        s.resize(R);
    }
    cin >> sangeunInput;
    cin >> N;
    otherInputs.resize(N);
    for (int i = 0; i < N; i++) {
        string i_temp;
        cin >> i_temp;
        otherInputs[i] = i_temp;
    }

    int each_score = calScore(sangeunInput, otherInputs);
    int max_score = calMaxScore(otherInputs);
    cout << each_score << endl;
    cout << max_score << endl;

    return 0;
}
```

# 풀이

그냥 점수를 계산하는 것은 쉬웠다.  
가능한 최대의 점수를 구하는 것이 어렵다기 보다는 문제 이해를 잘 못해서 시간을 잡아먹은 것 같다. 문제를 잘 읽자. 때문에 `set`, `map` 등 여러 STL 라이브러리를 찾아다니느라 시간을 소요한 것 같다.

가능한 최대 점수를 구하는 함수는 `int calMaxScore (StringVector all_in)`인데, 이 함수는 상근이를 제외한 다른 사람들의 모든 입력 결과 (`all_in`)을 인자로 받는다.  
`all_in`은 `string<vector>`형이며, 벡터 컨테이너는 라운드의 수, 그리고 한 컨테이너가 담고있는 `string`은 *상근이의 친구들이 각 라운드에 낸 모든 모양*들이다.  

이러한 정보를 담고 있는 `string<vector> all_in` 배열을 `string<vector> per_round_set`으로 바꾸려고 했는데, 이유는 *라운드를 고정시킨 채로 라운드별로 상근이의 친구들이 낸 모든 모양*을 담고 있는 벡터를 만들고 싶었기 때문이다.  

해당 벡터 변환 기능을 수행하는 우아한 함수가 있을 줄 알았는데 없었기 때문에 `StringVector toRoundSet (StringVector input)`으로 직접 구현하였다.  

그렇게해서 얻어진 벡터 `per_round_set`을 벡터 컨테이너 하나 별로 `vector<int> allPossibleScore(string round_set)`에 인자로 전달한다. 이 함수는 해당 라운드에서 상근이가 얻을 수 있는 가능한 보든 점수(`R`, `S`, `P`별 모든 점수)를 `int`형 벡터 컨테이너에 순서대로 담는다. `0`번 인덱스가 `R`을 냈을 때의 점수이고, `1`번 인덱스가 `S`를 냈을 때의 점수, `2`번 인덱스가 `P`를 냈을 때의 점수이다.  

그리고 나서 최종적으로 `calMaxScore`함수 내에서 `<algorithm>`라이브러리의 `max_element`함수를 이용하여 모든 가능한 상근이의 점수 중에서 최댓값을 구해, **라운드 별**로 더해주어 리턴한다.

# 총평

어렵지 않은 문제를 빙빙 돌아 푼 느낌이 든다....

# 더 알아보기

## 더 공부해야 할 사안들 

**STL 라이브러리**에 대해서 깊이 있는 공부를 한 적이 없어서 쓸 때마다 헷갈린다.  
주로 헷갈리는 사항들은 아래와 같다.

- STL 라이브러리를 초기화만 했을 때에 메모리는 어떻게 할당되어 있는가?
    - 예를 들어, 비어있는 `string`을 선언하면 어떻게 되지? 아무 내용이 없지만 일단 크기를 고정하고 싶으면 어떻게 해야 하나?
- STL 라이브러리를 값과 함께 초기화 하면, 값들의 숫자대로 크기가 정해지는가?
- STL 라이브러리를 함수의 입출력으로 사용할 때에 메모리 내에서 어떻게 저장되고, 참조되는가에 대해 멘탈 맵이 없다.

## 참조한 링크들

- `std::vector` 관련
    - [\[C++\] 배열 및 (STL) `vector` 초기화 방법 정리/Ressi](https://hini7.tistory.com/66#toc-1차원%20배열)
    - [How to `cin` values into a `vector`/Stackoverflow](https://stackoverflow.com/questions/8377660/how-to-cin-values-into-a-vector)
    - [\[C++\] STL Vector 사용법 & 예제 총정리/코딩팩토리](https://coding-factory.tistory.com/596)
- `std::string` 관련
    - [Allocating a length of new C++ `string` dynamically/cplusplus](https://cplusplus.com/forum/general/266230/)
- 최댓값, 최솟값 라이브러리 `<algorithm>`관련
    - [C++ Vector 최대값, 최소값, 인데스 구하기/](https://notepad96.tistory.com/40)
    - [C++ How to find the biggest key in a `std::map`?/Stackoverflow](https://stackoverflow.com/questions/1660195/c-how-to-find-the-biggest-key-in-a-stdmap)
- 기타 STL 관련
    - [C++ maps, hash tables, dictionaries(맵, 해시테이블, 딕셔너리) -only 간략한 개념 설명만/dr.meteor 공부 일지](https://thewayaboutme.tistory.com/150)
    - [[\[C++\] map container 정리 및 사용법/개발자 지망생](https://blockdmask.tistory.com/87)

