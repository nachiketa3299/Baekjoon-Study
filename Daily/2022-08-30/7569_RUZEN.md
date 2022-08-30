---
cdate: "2022-08-30T15:33:17"
vdate: 
  - "2022-08-30T15:33:17" # Created

isFail: true
ddate: 2022-08-30
boj_link: https://www.acmicpc.net/problem/7569
solve_times:
  - [2022-08-30T15:33, 2022-08-30T16:47]
---

# 7569

## 소요시간

## 문제 독해

토마토를 보관하는 큰 창고가 있다.
격자 모양 상자의 칸에 토마토를 하나씩 넣고, 상자를 수직으로 쌓아 올린다.

저장된 토마토 중에는 잘 익은 것도 있는데, 익지 않은 것도 있다.
보관 후에 하루가 지나면, 익은 토마토들의 *인접*한 곳에 있는 익지 않은 토마토들이 영향을 받아 익게 된다.

여기서 *인접* 이란 **위**, **아래**, **왼쪽**, **오른쪽**, **앞**, **뒤**, 여섯 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토 들은 서로 영향을 주지 못한다.
토마토가 혼자 저절로 익는 경우는 없다.

철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수가 알고 싶다.

입력으로는 첫 줄에 상자의 크기를 나타내는 두 정수 `M`과 `N`, 쌓아올리는 상자의 갯수인 `H`가 주어진다.
`M`은 상자의 가로, `N`은 상자의 세로이다. $2 \leq M \leq 200$, $2 \leq N \leq 100$, $1 \leq H \leq 100$이다.

둘째 줄부터 `N`개의 줄에는 가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토들의 정보가 주어진다.
한 줄에 하나의 상자에 담긴 토마토의 정보가 주어진다.
정수 `1`은 익은 토마토, 정수 `0`은 익지 않은 토마토, 정수 `-1`은 토마토가 들어있지 않은 칸을 나타낸다.
이러한 `N`개의 줄이 `H`번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.
토마토가 모두 익지는 못하는 상황이면 `-1`을 출력한다.

예제 입출력은 아래와 같다.

**예시 1**

```text
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
```

```text
-1
```

**예시 2**

```text
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
```

```text
4
```

**예시 3**

```text
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
```

```text
0
```


## 알고리즘

- 3차원 벡터로 토마토들을 관리해야 할 것 같다.

우선 모두 익을 수 있는 상황임을 판단해야 연산 시간을 줄일 수 있을 것 같다. 모두 익을 수 있는 상황일 때에만 얼마나 기다려야 모두 익는지에 대한 연산을 하면 될 것 같다. 그렇지 않은 상황이라면 `-1`을 리턴하기만 하면 된다.

- 함수: 모두 익을 수 있는 상황을 감지하는 함수
- 함수: 얼마나 기다려야 모두 익는지에 대한 연산을 하는 함수

[[14499|주사위 굴리기]] 문제에서 문제에서 제시된 데이터의 구조와 내가 만든 데이터의 구조의 불일치로 다른 답이 나왔었으므로, 이 문제에서는 처음부터 신경써서 구현하도록 한다.

## 소스코드

```cpp
#include <iostream>
#include <vector>

using namespace std;


typedef struct {
    int _x, _y, _z;
} Position3D;

typedef struct {
} RipeDirection3D;

class Tomato {
private:
    RipeDirection3D m_near;
    int m_ripe_state;
public: /* Constructor */
    Tomato (int ripe_state)
        : m_ripe_state(ripe_state) {}
};

typedef vector<vector<vector<Tomato>>> TGrid3D;

class Box {
private:
    Position3D m_hnm;
    TGrid3D m_grid;
    bool m_can_be_all_riped;
    bool m_is_all_riped;
public: /* Constructor */
    Box (Position3D hnm) : m_hnm(hnm) {}
public: /* General Functions */
    void put (Tomato t, Position3D pos) {
        this->m_grid[pos._z][pos._y][pos._x] = t;
        return;
    }
    void init (void) {
        this->_calCanBeAllRiped ();
        if (this->canBeAllRiped()) {
            this->_initTomato();
        } 
        return;
    }
    void ripe (void) {
        return;
    }
public: /* Getter */
    bool canBeAllRiped (void) {
        return this->m_can_be_all_riped;
    }
    bool isAllRiped (void) {
        for (auto n: this->m_grid) {
            for (auto m: n) {
                for (auto t: m) {
if
                }
            }
        }
        return this->m_is_all_riped;
    }
private:
    void _calCanBeAllRiped (void) {
        return;
    }
    void _initTomato (void) {
        return;
    }
};




int main (void) {
    int M, N, H;
    cin >> M >> N >> H;
    Box box (Position3D { H, N, M });

    for (int h = 0; h < H; h++) {
        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                int ripe_state;
                cin >> ripe_state;
                Tomato tomato (ripe_state);
                box.put(tomato, Position3D { h, n, m });
            }
        }
    }

    box.init();
    int days;
    if (box.canBeAllRiped()) {
        days = 0;
        while (box.isAllRiped()) {
            box.ripe();
            days++;
        }
    } else {
        days = -1;
    }

    cout << days << endl;

    return 0;
}

```

# Reference

## 참고한 것

## 더 하고싶은 것

구현부터 차근차근 했는데 알고리즘을 짜다가 제한 으로 두었던 1시간 20분에 근접하여 실패로 처리했다.
아직 공부할 것이 많다. 클래스 관리하는 것이 미숙해서 속도가 안 붙는 듯 하다.
궁금한 것은 모든 토마토가 익었는지 확인하려면 어쩔 수 없이 3개의 `for`문을 돌려야 하는 것 같은데, 이게 올바른 방법인 건지 감이 오지 않는다.
