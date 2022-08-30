---
aliases:
  - 설탕 배달
cdate: "2022-08-24T11:42:06"
vdate: 
  - "2022-08-24T11:42:06" # Created
boj_link: https://www.acmicpc.net/problem/2839
solve_times: 
  - ["2022-08-24T11:39", "2022-08-24T12:14"] # 35 min
---

# 2839

## 소요시간

- 풀이 작성 및 풀이 완료까지 35분

## 문제 독해

- 설탕 봉지는 3kg짜리랑 5kg짜리 두 개만 있다.
- 상근이가 설탕 배달 kg 단위로 한다.
- 귀찮으니까 최대한 적은 봉지의 숫자로 배달 요구 kg을 맞춰서 배달하려고 한다.
    - 예를 들어 18kg 설탕 배달 하려면 3kg \* 6이 아니라, 5kg \* 3 + 3kg \* 1개로 하려고 한다.
- 상근이가 정확히 N킬로그램의 설탕을 배달해야 할 때, 봉지를 몇 개 가져가야 하는가? 정확히 N킬로그램을 만들 수 없으면 `-1`을 출력하면 된다.

## 알고리즘 생각

- `N`을 입력 받는다. `N in [3, 5000]`
- 5로 나눈 후 몫 `con_5` 과 나머지 `mod_5` 를 저장한다.
- `mod_5`을 3으로 나누었을 때,
    - 나머지 `mod_3`이 0이면, `mod_5`를 3으로 나눈 몫을 `con_3`을 저장한다.
    - 나머지 `mod_3`이 0이 아니면, `-1`을 **리턴**한다.
- `con_5`와 `con+3`을 **리턴**한다.

너무 쉬운데? 뭔가 함정이 있나 싶었는데 역시나였다.

- 코딩을 하기 전에 예제 출력들을 하나씩 알고리즘에 넣어봤는데  바로 반례를 발견했다. (…)
    - 입력이 `9`이면 출력이 `3`이어야 하는데, 내 알고리즘은 `-1`을 리턴한다.
    - 입력이 `9`인 경우 5kg짜리 봉지를 하나 사용하는 순간 `4`가 되는데, 이 경우 3kg만으로 만들 수 없어서 `-1`을 리턴한다.
- **5kg봉지를 반드시 (최대로) 사용해야 하는 것은 아니다!!**

최대로 사용할 수 있는 5kg 봉지의 갯수를 정하고, 하나씩 줄여가는 방법으로 알고리즘을 다시 짜봤다.

- `N`을 입력 받는다. `N in [3, 5000]`
- 5로 나눈 후 몫 `con_max_5`을 저장한다.
- `for`문을 인덱스 `i`가 `con_max_5`이하부터 `0` 이상일 때까지 실행한다:
    - `i` 는 현재 상태에서 사용한 5kg의 봉지의 숫자고, 따라서 해당 상황에서 남은 설탕의 kg수인 `mod_5`를 `N - i * 5`를 하여 구한다.
    - `mod_5`를 3으로 나눈 몫 `con_3`과 나머지 `mod_3`을 구한다.
        - `mod_3 == 0` 인 경우, `i + con_3`을 리턴한다.
        - `mod_3 != 0`인 경우, 반복문을 계속 진행한다.
- 만약 리턴이 발생하지 않고 반복문이 종료되었을 경우, `-1`을 리턴한다.

리턴으로 반복문을 탈출하도록 코드를 짤 것이므로 위 알고리즘을 함수에 담을 것이다. 아마도 아래처럼 되겠지.

```cpp
const int calMinContainer (const int N) {
    const int con_max_5 = N / 5;

    for (int i = con_max_5; i >= 0; i--)  {
        const int mod_5 = N - (i * 5);
        const int mod_3 = mod_5 % 3;

        if (mod_3 == 0) {
            const int con_3 = mod_5 / 3;
            return i + con_3;
        } else {
            ;
        }
    }

    return -1;
}
```

한가지 궁금증이 들었는데, 위 코드는 **5kg 봉지의 갯수가 최대일 때, 전체 봉지의 갯수가 최소이다** 라는 전제 위에서 짠 것이다.  
가만 생각해보니 당연하다. 5kg 봉지를 하나 사용하지 않음으로서 추가적으로 만들어지는 3kg 봉지는 최소 한 개이다. 

## 최종 소스 코드

```cpp
#include <iostream>

using namespace std;

const int calMinContainer (const int N) {
    const int con_max_5 = N / 5;

    for (int i = con_max_5; i >= 0; i--)  {
        const int mod_5 = N - (i * 5);
        const int mod_3 = mod_5 % 3;

        if (mod_3 == 0) {
            const int con_3 = mod_5 / 3;
            return i + con_3;
        } else {
            // Nothing
        }
    }

    return -1;
}

int main (void) {

    // (3 <= N <= 5000)
    int N;
    cin >> N; 
    cout << calMinContainer(N) << endl;


    return 0;
}
```

## 궁금한 것

- 제어문에서 아무것도 안 하는 경우 파이썬에선 `pass`를 썼던 것 같은데, C++에선 무엇을 쓰는가?
    - [Is there an equivalent of Python's `pass` in c++std11?/Stackoverflow](https://stackoverflow.com/questions/20382278/is-there-an-equivalent-of-pythons-pass-in-c-std11)
        - 간단하게 `{}`만 쓰거나, `;`만 쓴다고 한다.
- 봉지의 무게를 변수로 받는, 일반화된 코드로 바꿔볼 순 없을까? → 나중에 해보기