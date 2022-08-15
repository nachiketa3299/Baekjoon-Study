---
use_math: true
---

# 소요 시간

- `[2022-08-15T10:27, 2022-08-15T11:48]`
- `[2022-08-15T13:48, 2022-08-15T15:01]`

총 **154분**

# 실패 코드

- 실패 사유: **시간 초과**

```cpp
#include <iostream>
#include <bitset>

using namespace std;
#define BS_MAX_SIZE 32
typedef bitset<BS_MAX_SIZE> Bitstream;


const int countOne (Bitstream B) {
    int count;
    for (int i = 0; i < B.size(); i++) {
        if (B[i] == 1) {
            count++;
        }
    }
    return count;
}

bool verify (Bitstream B, int K) {
    if (countOne(B) <= K) {
        return true;
    } else {
        return false;
    }
}

Bitstream increment (Bitstream B) {
    for (int i = 0; i < B.size(); i++) {
        if (B[i] == 0) {
            B[i] = 1;
            break;
        }
        B[i] = 0;
    }
    return B;
}

int main (void) {
    // Input N, K (N <= 10'000'000, K <= 1'000)
    int N, K;
    cin >> N >> K;


    const Bitstream BN (N);
    Bitstream TB (BN);

    while (!verify(TB, K)) {
        TB = increment(TB);
    }

    int answer = static_cast<int>(TB.to_ulong() - BN.to_ulong());

    return 0;
}
```

# 풀이

간단하게 생각했다. 

$2^0L$, $2^1L$, $2^2L$, ... 해당 $L$의 용량을 지닌 물통을 배치할 수 있는 구획들이 있다고 가정했다.  
그리고, 해당 구획에 물통이 2개가 되면, 하나로 합쳐서 다음 구획으로 이동시킨다.

우선 초기에 주어지는 $1L$짜리 물통들을 규칙에 맞게 합쳐서, 위에서 정의한 구획들에 배치한다.  

그러면 각 구획 별로 1개 아니면 0개의 물통이 배치될 것이다. 

이 물통들의 전체 갯수를 $bin(N)$이라 했을 때, $Bin(N) \leq K$가 되도록 상점에서 $1L$짜리 물을 얼마나 가져올 것인가, 이것이 문제의 목표이다.  

내가 짠 알고리즘은 아래와 같다.

1. 초기에 주어지는 $1L$짜리 물통들을 규칙에 맞게 합쳐서, 정의한 구획들에 배치한다.
2. 물통의 총 갯수를 $bin(N)$을 구한 후 $bin(N) \leq K$이 성립하는지 확인한다.
3. 성립하지 않는다면 상점에서 $1L$짜리 물을 하나 가져와, 구획에 배치한다. 그리고 다시 2번째 단계로 돌아간다. 
4. 성립한다면 이제까지 상점에서 빌려온 물통의 갯수 $T$를 구하여 출력한다.

답은 제대로 출력하였지만, 제출시 시간 초과가 발생했다.  
생각해보면 시간 초과가 발생하는 것은 당연한데, 왜냐하면 적당히 작은 $N$에 대해서는 상점에서 $1L$짜리 물을 계속 빌려와도 상관이 없지만, 만약 $N = 1000000$과 같은 상황에서는 상점에서 물을 빌려오는 연산에 부하가 걸릴 것이 확실하기 때문이다.  

사실 답을 내는 데에는 문제가 없으나..., 백준이 틀렸다는데 어쩌겠는가.

- *P.S. 위에서 '구획'이라고 표현했지만, 사실 수학적으로 표현하면 이 문제는 **이진수의 연산**으로 환원할 수 있다.*

# 참조 링크

C++에서 10진수를 2진수로 바꿔주는 STL 라이브러리 `bitset`에 대해서 많이 찾아보았다.  
이 라이브러리는 고정된 길이의 이진수 비트의 저장과 비트단위(bitwise)연산은 지원하는게 많았으나, 산술(arithmetic)연산은 지원하지 않아서 조금 더 찾아보아야 했다.

- [C++에서 Decimal을 Binary로 변환하는 방법](https://www.delftstack.com/ko/howto/cpp/how-to-convert-decimal-number-to-binary-in-cpp/)
- [`std::bitset`/cppreference](https://cplusplus.com/reference/bitset/bitset/)
- [\[STL\] Bitset 생성 및 초기화 방법/Notepad](https://notepad96.tistory.com/35)
- [How can I increment `std::bitset`/Stackoverflow](https://stackoverflow.com/questions/16761472/how-can-i-increment-stdbitset)

# 그래서 어떻게 풀어야 할까

사실 처음에 이진수에 +1을 답이 될 때까지 연산하는 것 외에 다른 방법을 생각하긴 했었다.  

뭐 예를 들어 사실 +1을 하는 이유가 자릿수를 계속해서 옮기기 위함인데, 비트 단위 연산자인 `<<`같은 것을 쓰면, 연산에 대한 부담을 줄이면서 소기의 목적을 달성할 수 있다.  

메모는 +1 이진수 연산의 비트단위 연산으로의 추상화라고 적어두긴 했는데, 아직 알고리즘을 짜진 못했다. 