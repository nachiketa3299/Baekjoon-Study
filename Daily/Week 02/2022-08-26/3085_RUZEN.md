---
boj_link: https://www.acmicpc.net/problem/3085
solve_times:
  - [2022-08-26T14:40, 2022-08-26T15:02]
  - [2022-08-26T15:09, 2022-08-26T16:19]
---

# 3085

## 소요시간

- 92분

## 문제 독해

- $N \times N$ 크기의 보드에 사탕을 채워넣는다.
- 사탕의 색상은 `C`, `P`, `Z`, `Y`의 4가지이다.
- 사탕의 색이 다른 인접한 *두 칸*을 고른다.
- 고른 두 칸에 들어있는 사탕을 서로 *교환*한다.
- 이제 모두 같은 색으로 이루어져 있는 가장 긴 연속부분(행/열)을 고른 후, 그 사탕을 모두 먹는다.
- 사탕이 채워진 상태가 주어졌을 때, **먹을 수 있는 사탕의 최대 개수는?**

1. 보드 판의 크기와, 사탕의 배치도를 받는다.
2. 사탕 두 개를 고른다.
    - 고르는 두 사탕은 서로 인접해야 한다.
    - 고르는 두 사탕은 색이 서로 달라야 한다.
4. 고른 사탕 두개를 바꾼다.
5. 같은 색으로 열/행으로 나열된 가장 긴 연속부분의 최대값을 구한다.


## 소스 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define HOR 0
#define VER 1

using namespace std;

class Board {
private:
    int _N;
    vector<string> _board;
public:
    Board (int N)
    : _N(N) {
        this->_board.resize(this->_N);
        for (string &s: this->_board) {
            s.resize(this->_N);
            cin >> s;
        }
    }
public: 
    int getMaxRowColItem (void) {
        int result = 1;

        // Horizontal direction checking
        for (int i = 0; i < this->_N; i++) {
            int hor_temp = 1; 
            for (int j = 1; j < this->_N; j++) {
                if (this->_board[i][j - 1] == this->_board[i][j]) {
                    hor_temp++;
                } else {
                    result = max(result, hor_temp);
                    hor_temp = 1;
                }

            }
            result = max(result, hor_temp);
        }

        // Vertical direction checking
        for (int i = 0; i < this->_N; i++) {
            int ver_temp = 1;
            for (int j = 0; j < this->_N - 1; j++) {
                if (this->_board[j + 1][i] == this->_board[j][i]) {
                    ver_temp++;
                } else {
                    result = max(result, ver_temp);
                    ver_temp = 1;
                }
            }
            result = max(result, ver_temp);
        }
        return result;
    }

    void swapCandy (int mode, int i, int j) {
        if (mode == HOR) {
            swap(this->_board[i][j], this->_board[i][j + 1]);
        } else {
            swap(this->_board[j][i], this->_board[j + 1][i]);
        }
        return;
    }

public: // Getter
    int getSize (void) {
        return this->_N;
    }

public: // for debug
    void printBoard (void) {
        for (auto l: this->_board) {
            for (auto c: l) {
                cout << c << " ";
            }
            cout << endl;;
        }
        return;
    }

};

int main (void) {
    // Colors: C, P, Z, Y
    int N;
    cin >> N; // (3 <= N <= 50)  
             
    Board B(N);

    int result = 0;
    for (int i = 0; i < B.getSize(); i++) {
        for (int j = 0; j < B.getSize() - 1; j++) {
            B.swapCandy(HOR, i, j);
            result = max(result, B.getMaxRowColItem());
            B.swapCandy(HOR, i, j);

            B.swapCandy(VER, i, j);
            result = max(result, B.getMaxRowColItem());
            B.swapCandy(VER, i, j);
        }
    }

    cout << result << endl;

    return 0;
}
```

## 풀이

뭔가 방법이 있을 줄 알았는데, 그냥 무식하게 열별로, 행별로 하나씩 다 뒤집어 보면서 그때그때 최대값을 구하니까 답이 나왔다. 다른 사람들은 어떻게 풀었는가 정말 궁금하다.

## 참조한 링크

- [C++ 09.10 - `this` 포인터/소년코딩](https://boycoding.tistory.com/25ㅁ0)
- [C++ - Algorithm 헤더 파일 - `swap()`, `swap_ranges()`, `copy()`, `fill()`/습관처럼](https://dev-mystory.tistory.com/219)
