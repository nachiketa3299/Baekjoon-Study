<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
# 풀이 시간

- `[2022-08-14T13:55, 2022-08-14T14:23]`
- `[2022-08-14T15:53, 2022-08-14T16:32]` 성공!
- 풀이에 걸린 시간 **총 67분**

# 소스 코드

```cpp
#include <iostream>
#include <string>

using namespace std;

string * getInput (int i_n) {
    string * str_arr = new string [i_n];
    for (int i = 0; i < i_n; i++) {
        cin >> str_arr[i];
    }
    return str_arr;
}

string genQuery (string * str_arr, int str_arr_size) {
    const int str_size = str_arr[0].length();
    string query;
    query.resize(str_size);

    // 스트링 들의 c_i번째 인덱스가 모두 같은지, 하나라도 다른지 판별
    for (int c_i = 0; c_i < str_size; c_i++) {
        bool is_all_same = true;
        for (int str_i = 1; str_i < str_arr_size; str_i++) {
            if (str_arr[0][c_i]  != str_arr[str_i][c_i]) {
                is_all_same = false;
                break;
            }
        }
        // 모두 같은지 하나라도 다른지 판별 결과에 따라 문자 할당
        if (is_all_same && str_arr[0][c_i] == '.') {
            query[c_i] = '.';
        } else if (is_all_same) {
            query[c_i] = str_arr[0][c_i];
        } else {
            query[c_i] = '?';
        }
    }

    return query;
}

int main (void) {
    /* Get string inputs */
    int N; // Number of file names
    cin >> N;
    string * str_arr = getInput(N);
    // str_arr[*].length() is all same

    cout << genQuery (str_arr, N) << endl;
    return 0;
}
```

# 풀이

`str_arr` 에 입력받은 `N`개의 문자열이 저장된다.  
다음의 검사 반복문을 작성하는 데에 가장 오랜 시간이 들었다.

|`c`|`o`|`n`|`f`|`i`|`g`|`?`|`?`|`?`|`?`|
|---|---|---|---|---|---|---|---|---|---|
|`c`|`o`|`n`|`f`|`i`|`g`|`.`|`s`|`y`|`s`|
|`c`|`o`|`n`|`f`|`i`|`g`|`?`|`i`|`n`|`f`|
|`c`|`o`|`n`|`f`|`i`|`g`|`u`|`r`|`e`|`s`|

Row별로 검사하도록 반복문을 구성했다. (열 번호를 `c_i`라고 이름붙였다.)  

<div class="mermaid">
graph TD; S["Start<br><code>c_i</code>별로 <code>str_arr</code>의 모든 문자열에 대해 비교"]; 0{"해당 열의 문자가 <br>모두 같은가?"}; 1{"모든 문자가 <code>.</code>인가?"}; 2["<code>qwery[c_i] = '?'</code>"]; 3["<code>qwery[c_i] = '.'</code>"]; 4["<code>qwery[c_i] = '*'</code><br><i>(해당 문자 대입)</i>"]; S ---> 0; 0 --->|"Yes"| 1; 0 --->|"No"| 2; 1 --->|"Yes"| 3; 1 --->|"No"| 4;
</div>

# 질문 사항

- *특정 집합의 원소가 모두 같은지 아닌지 판단하는 알고리즘*인 것 같은데, 더 좋은 방법이 있는지 궁금하다.
- `string` 자료형을 선언하는 방법이 헷갈렸다. 항상 `string str = 'abcd'`와 같은 방법으로 사용했어서 그런 것 같다.
    - `string` 변수를 선언할 때에 내용물과 길이를 명시하는 방법은?

# 개선 사항

`string * str_arr` 형태로 입력받은 문자열들을 `string`형 배열로 관리했다. 배열을 사용하는 방법의 문제는 함수로 전달할 때에 배열의 크기를 같이 넘겨줘야 한다는 것이다. 예를 들어 `string genQuery (string * str_arr, int str_arr_size)`처럼 말이다.  

더 우아한 방식을 심지어 알고 있었는데 C언어 배울 때 배열을 하도 많이 써서 그런가 자연스럽게 저렇게 짰다. 위 코드가 틀린건 아니지만, `vector`라이브러리(STL)를 이용하면 훨씬 더 우아하게 코드를 줄일 수 있겠다는 생각을 했다. 위 코드는 사실 문제가 있는데, `getInput`함수에서 동적으로 할당한 메모리를 명시적으로 `delete`해주지 않고 있기 때문이다. 마지막에 `delete [] str_arr;`을 추가해주면 되지만, ... `vector`는 자동으로 메모리를 정리해 주기 때문에 `vector`를 쓰는 것이 이 경우에는 더 낫다고 생각된다.

- [\[C++\] vector container 정리 및 사용법/개발자 지망생](https://blockdmask.tistory.com/70)

위 링크의 도움을 받아, 코드를 개선해 보았다.

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> getInput (int i_n) {
    vector<string> str_vec(i_n);
    for (int i = 0; i < i_n; i++) {
        cin >> str_vec[i];
    }
    return str_vec;
}

string genQuery (vector<string> str_vec) {
    const int str_vec_size = str_vec.size();
    const int str_size = str_vec[0].length();
    string query;
    query.resize(str_size); 

    // 스트링 들의 c_i번째 인덱스가 모두 같은지, 하나라도 다른지 판별
    for (int c_i = 0; c_i < str_size; c_i++) {
        bool is_all_same = true;
        for (int str_i = 1; str_i < str_vec_size; str_i++) {
            if (str_vec[0][c_i]  != str_vec[str_i][c_i]) {
                is_all_same = false;
                break;
            }
        }
        // 모두 같은지 하나라도 다른지 판별 결과에 따라 문자 할당
        if (is_all_same && str_vec[0][c_i] == '.') {
            query[c_i] = '.';
        } else if (is_all_same) {
            query[c_i] = str_vec[0][c_i];
        } else {
            query[c_i] = '?';
        }
    }

    return query;
}

int main (void) {
    /* Get string inputs */
    int N; // Number of file names
    cin >> N;
    vector<string> str_vec = getInput(N);
    // str_vec[*].length() is all same

    cout << genQuery(str_vec) << endl;

    return 0;
}
```

# 더 알아볼 것

- `string`, `vector`, `array` 등 STL의 사용법에 대한 정리. (정확히 말하면 `string`은 STL이 아니라고 한다.)