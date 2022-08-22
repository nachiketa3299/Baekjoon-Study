# 풀이 시간

- `[2022-08-22T12:00, 2022-08-22T12:08]`
- 총 8분

# 소스 코드

```cpp
#include <iostream>

using namespace std;

int calSumDecom (const int input) {
    int i_t = input;
    int digit_sum = 0;
    while (i_t != 0) {
        digit_sum += i_t % 10;
        i_t /= 10;
    }
    return input + digit_sum;
}

int main (void) {
    int N; 
    cin >> N;

    int smallest_gen = 0;
    for (int i = 1; i < N; i++) {
        if (calSumDecom(i) == N) {
            smallest_gen = i;
            break;
        }
    }

    cout << smallest_gen << endl;
    return 0;
}
```

# 풀이

분해합을 구하는 함수 `calSumDecom`을 만든다.
`N`이 주어졌다면, 1부터 `N`까지의 순서대로 `calSumDecom`을 하여, 결과가 `N`과 같아지는 경우 그것이 정답이다.
다만, 분해합이 없는 경우 답이 0이 되도록 신경 써주어야 한다.

# 총평

제가 고른 문제지만 너무 쉽네요. 죄송합니다.