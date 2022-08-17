# 풀이 시간 

- `[2022-08-15T23:32, 2022-08-15T02:01]` 153
- `[2022-08-16T09:21, 2022-08-16T09:41]` 20
- 총 173분

# 제출 코드

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int cAbstract(int N, int r, int c) {
    if (r < pow(2, N - 1)) {
        if (c < pow(2, N - 1)) {
            return 0;
        } else {
            return 1;
        }

    } else {
        if (c < pow(2, N - 1)) {
            return 2;
        } else {
            return 3;
        }
    }
}

int cArea (int N) {
    return static_cast<long int>(powl(2, 2 * N));
}

int crmap (int N, int r) {
    int new_r;
    if (r < pow(2, N - 1)) {
        new_r = r;
    } else {
        new_r = r - pow(2, N - 1);
    }
    return new_r;
}
int ccmap (int N, int c) {
    int new_c;
    if (c < pow(2, N - 1)) {
        new_c = c;
    } else {
        new_c = c - pow(2, N - 1);
    }
    return new_c;
}

int AB (int N, int r, int c) {
    if (N > 1) {
        int vpos = cAbstract(N, r, c);
        int pastCount = vpos * cArea(N - 1);
        return pastCount + AB(N - 1, crmap(N, r), ccmap(N, c));

    } else {
        return cAbstract(N, r, c);
    }
}

int main (void) {
    int N, r, c;
    cin >> N >> r >> c;
    cout << AB(N, r, c) << endl;

    return 0;
}
```

# 풀이

사등분 하여 몇 사분면에 속하는지 확인하는 것을 더이상 사등분 할 수 없을 때까지 반복하고 더해줍니다.

1. 함수 `AB`를 구현하였다. `AB(N, r, c)`는, $2^N$을 한 변의 길이로 가진 이차원 배열의 `r`행 `c`열의 원소의 탐색 순서를 리턴한다.
2. `cAbstract(N, r, c)` 함수는 $2^N$을 한 변의 길이로 가진 이차원 배열을, $2^{N-1}$을 한 변으로 가지도록 사등분 했을 때, `r`행 `c`열의 원소가 몇 사분면에 오는지 리턴한다. 
    - 참고로 사분면은 좌상단, 우상단, 좌하단, 우하단 순으로 0, 1, 2, 3을 리턴한다.
3. `AB`함수에서, 만약에 $N$이 1이라면, `cAbstract(1, r, c)`의 반환값이 곧 정답일 것이므로 이를 리턴한다.
4. 하지만 만약에 $N$이 1이 아니라면, `AB`함수 내에서 `pastCount + AB(N - 1, crmap(N, r), ccmap(N, c))`를 리턴한다. 재귀 함수이다.
    - 만약에 `cAbstract(N, r, c)`의 결과로 2가 나왔다면, `r`행 `c`열의 원소가 속한 사분면은 3번째로 탐색된다.
    - 때문에 `r`행 `c`열의 원소는 0, 1 사분면을 지나왔을 것이고 해당 사분면에서 각 사분면 별로 사분면에 속한 원소의 갯수만큼 탐색을 진행했을 것이다. 이를 나타내는 것이 `pastCount`이다.
    - 그리고 `AB(N - 1, crmap(N, r), ccmap(N, c))`를 다시 호출한다. 이 경우 `N - 1`에 대해서 새로 호출하는데, `crmap`, `ccmap`함수로 `r`행 `c`열 이라는 좌표를 새로 매핑하고 있다. 예를 들어 `r`행 `c`열이 3사분면에 있다면, 우리는 3사분면을 *다시* 4등분 하여 위 과정을 반복할 것이므로, 새로운 `r`과 `c`를 넣어주어야 하는데 이것을 구하는 함수가 `crmap`, `ccmap`이다.
5. $N = 1$인 경우 더이상 사등분 할 수 없으므로 (`cAbstract`의 결과가 곧 순서이므로) 이제까지 호출된 재귀 함수들을 차례로 종료하면서 `pastCount`들을 더해준다.

# 총평

그렇게 어렵지는 않았는데 자잘한 오류가 자꾸 나서 시간을 잡아먹은 것 같다.  
특히 `cramp`과 `ccmap`함수를 만드는 데에서 실수가 있어서 마지막 테스트 케이스인 `10 512 512`에 대해서 오류가 났다.  
해당 함수가 `N`에 의존적이게 짰어야 했는데, 처음에는 그렇지 않게 짰기 때문이다. (다른 케이스에서 답이 제대로 나온 것이 신기하다.)

# 도움이 된 링크들

- C++이 함수 내에서 함수를 선언할 수 있는지 (그냥) 궁금했는데 [C++ 함수 안에 함수 정의/서의 공간](https://chaoyue.tistory.com/185)에서 확인한 바, C/C++에서는 *Nested Subroutine*을 지원하지 않는다고 한다.
- [Use of `const` for function parameters/Stackoverflow](https://stackoverflow.com/questions/117293/use-of-const-for-function-parameters) 함수 선언시 입력 파라미터와 출력 타입에 `const`를 붙이는 것이 장황하고 불필요하다고까지 느껴졌는데 해당 게시물을 참조한다. (아직 안읽어봄)

