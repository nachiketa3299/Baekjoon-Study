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

`str_arr` 에 입력받은 문자열이 저장된다.

<style>
    .heatMap th {
        background: blue;
    }
</style>


|`c`|`o`|`n`|`f`|`i`|`g`|`?`|`?`|`?`|`?`|
|---|---|---|---|---|---|---|---|---|---|
|`c`|`o`|`n`|`f`|`i`|`g`|`.`|`s`|`y`|`s`|
|`c`|`o`|`n`|`f`|`i`|`g`|`?`|`i`|`n`|`f`|
|`c`|`o`|`n`|`f`|`i`|`g`|`u`|`r`|`e`|`s`|



