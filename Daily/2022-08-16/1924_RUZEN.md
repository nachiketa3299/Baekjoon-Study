# 풀이 시간

- [2022-08-15T18:18, 2015-08-15T19:11] 53
- 총 53분

# 제출 코드

```cpp
#include <iostream>
#include <string>
#define BASE_MONTH 1
#define BASE_DAY 1

using namespace std;

class Calendar {
private:
    const int y = 2007;
    int month;
    int day;
    int fullday;
public:
    Calendar (int m, int d)
        :month(m), day(d)  {
        const int m_l_d[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int full_month_days = 0;
        for (int i = BASE_MONTH; i < this->month; i++) {
            full_month_days += m_l_d[i - 1];
        }
        this->fullday = full_month_days + this->day - BASE_DAY;
        return;
    }
    const string getDow (void) {
        const string dow_list[7] = {
            "MON"
            , "TUE"
            , "WED"
            , "THU"
            , "FRI"
            , "SAT"
            , "SUN"
        };
        return dow_list[this->fullday % 7];
    }
};

int main (void) {
    int x, y;
    cin >> x >> y;
    Calendar today (x, y);

    cout << today.getDow() << endl;
    return 0;
}
```

# 풀이

- `Calendar` 객체를 만들어서, 입력받은 `x`월 `y`일로 초기화 한다.  
`fullday` 멤버 변수에 1월 1일부터 `x`월 `y`일 까지의 총 일수를 넣는다. 
- `getDow` 멤버 함수는 `fullday` 멤버 변수를 `7`로 나눈 나머지를 통해서 무슨 요일인지 반환한다.

# 도움 받은 링크들

- C++에서 클래스 내에서 자신을 인스턴스로 선언할 수 없다. [클래스 안에서 자기자신의 인스턴스를 멤버변수로 사용해도 되나/GPGSTUDY 포럼](https://www.gpgstudy.com/forum/viewtopic.php?t=11450)
