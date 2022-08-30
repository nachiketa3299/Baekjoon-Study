# 풀이시간

- `[2022-08-22T11:33, 2022-08-22T11:44]`
- `[2022-08-22T11:51, 2022-08-22T11:59]`

# 소스코드

```cpp
#include <iostream>
#include <vector> // array and vector difference?

using namespace std;

typedef struct {
    int weight;
    int height;
} WeHeight;

const bool isSmall (WeHeight current, WeHeight compare) {
    if (current.weight < compare.weight) {
        if (current.height < compare.height) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

const int findRank (const int index, vector<WeHeight> arr) {

    WeHeight current = arr[index];
    int current_rank = 1;

    for (int i = 0; i < arr.size(); i++) {
        if (isSmall(current, arr[i]) && i != index) {
            current_rank++;
        }
    }
    return current_rank;
}

int main (void) {
    int N; // (2 <= N <= 50)
    cin >> N; // (10 <= x, y <= 200)

    vector<WeHeight> parr;
    for (int i = 0; i < N; i++) {
        int input_temp_w, input_temp_h;
        cin >> input_temp_w >> input_temp_h;
        parr.push_back(WeHeight{ input_temp_w, input_temp_h });
    }

    vector<int> rankarr;

    for (int i = 0; i < parr.size(); i++) {
        rankarr.push_back(findRank(i, parr));
    }

    for (auto e: rankarr) {
        cout << e << " ";
    }

    return 0;
}
```

# 풀이

몸무게와 키를 포함하고 있는 구조체 타입 `WeHegith`를 선언하고, 이 타입으로 이루어진 벡터 어레이 `parr`를 선언한다.
입력받은 몸무게와 키를 받아 `parr`에 저장한다.
`parr`을 순회하면서 각 요소의 등수를 측정하는 `findRank`함수를 호출한다.


# 더 알아볼 것 && 더 해볼 것

- `<array>` 와 `<vector>`는 다른점이 무엇이고 각각 언제 사용하는 것인가?
- 구조체가 아닌 클래스로 선언하여 비교 연산자를 오버로딩 하면 `isSmall`함수를 사용하지 않아도 될 것 같다.