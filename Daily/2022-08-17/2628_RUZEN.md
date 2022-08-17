# 풀이 시간

- `[2022-08-17T15:16, 2022-08-17T16:42]` 86분
- 총 **86** 분

# 소스 코드

```cpp
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

#define HOR 0
#define VER 1

using namespace std;

typedef struct {
    int x;
    int y;
} Points;

typedef struct {
    int mode;
    int index;
} SliceInfo;

class Rectangle {
    private:
        Points _rec_points[2];
        int _w;
        int _h;
        int _area;
    public:
        Rectangle (Points i0, Points i1) {
            this->_rec_points[0] = i0;
            this->_rec_points[1] = i1;
            this->_w = abs(_rec_points[0].x - _rec_points[1].x);
            this->_h = abs(_rec_points[0].y - _rec_points[1].y);
            this->_area = this->_w * this->_h;
            return;
        }
        int getArea (void) {
            return this->_area;
        }
        Points * getPoints (void) {
            return this->_rec_points;
        }
};

class SliceTable {
    private:
        Rectangle _R;
        vector<Rectangle> _subR;
        vector<SliceInfo> _slice_info;
        vector<int> hor_index{0};
        vector<int> ver_index{0};
    public:
        SliceTable (Rectangle main_rec) 
        :_R(main_rec){
        }
        void saveSliceInfo(SliceInfo info) {
            this->_slice_info.push_back(info);
            return;
        }
        void slice () {
            for (auto &e: this->_slice_info) {
                if (e.mode == VER) {
                    this->ver_index.push_back(e.index);
                } else {
                    this->hor_index.push_back(e.index);
                }
            }
            this->ver_index.push_back(_R.getPoints()[1].x);
            this->hor_index.push_back(_R.getPoints()[1].y);

            sort(this->ver_index.begin(), this->ver_index.end());
            sort(this->hor_index.begin(), this->hor_index.end());

            for (int v = 1; v < this->ver_index.size(); v++) {
                for (int h = 1; h < this->hor_index.size(); h++) {
                    Rectangle sub_rec(Points {this->ver_index[v - 1], this->hor_index[h - 1]}, Points {this->ver_index[v], this->hor_index[h]});
                    this->_subR.push_back(sub_rec);
                }
            }
            return;
        }
        int findMaxSubRectangleArea (void) {
            vector<int> sub_rec_areas;
            for (auto &r: this->_subR) {
                sub_rec_areas.push_back(r.getArea());
            }
            int max_area = *max_element(sub_rec_areas.begin(), sub_rec_areas.end());
            return max_area;
        }
};

int main (void) {
    int W, H;
    int slice_num;
    cin >> W >> H;
    cin >> slice_num;
    Rectangle R = Rectangle(Points{ 0, 0 }, Points{ W, H });
    SliceTable S = SliceTable (R);
    for (int i = 0; i < slice_num; i++) {
        SliceInfo slice_info;
        cin >> slice_info.mode >> slice_info.index;
        S.saveSliceInfo(slice_info);
    }
    S.slice();
    cout << S.findMaxSubRectangleArea() << endl;
    
    return 0;
}
```

# 풀이

## 알고리즘 흐름

`Rectangle`이라는 클래스를 만든다. 이 클래스는 `Points` 구조체 2개로 사각형을 정의한다. (대각 방향의 두 점으로 사각형을 정의하는 것이다.)  
최초로 입력받은 `W`, `H`를 이용해 하나의 `Rectangle R` 인스턴스를 만들고, 이를 이용해 `SliceTable S` 이라는 객체를 만든다.  
이름이 뜻하는 대로 이 행위는 사각형을 자르기 위해 테이블 위에 올려놨다는 뜻이다.  

사각형을 올려논 후, `SliceInfo` 구조체를 이용해 어디를 어떻게 자를 것인지에 대한 정보를 입력받고 `SliceTable` 객체에 저장한다.  
모든 자르기 정보를 입력받은 후에는, `S.slice()`를 이용해 자른다.  
이 함수가 호출되면, `SliceTable S` 객체 내의 정보를 이용해 `R`을 쪼개어, 쪼갠 후 만들어진 사각형들을 역시 `Rectangle` 클래스를 이용해 `S`에 저장한다.

`S`는 `S.slice()`호출 후 쪼개진 사각형들에 대한 배열을 가지고 있고, `S.findMaxSubRectangleArea()`를 통해서 이 중에서 가장 큰 넓이를 갖는 사각형의 넓이를 반환할 수 있다.

## 가장 중요한 부분: 어떻게 쪼갤 것인가

세로로 쪼개는 인덱스와 가로로 쪼개는 인덱스를 나누어 생각했다.  
세로로 쪼개는 인덱스는 `0`, `v1`, `v2`, ... `W`이고, 가로로 쪼개는 인덱스는 `0`, `h1`, `h2`, ... , `H` 이다.
이 인덱스들을 이용해 2중 `for`문을 만들면 만들어지는 사각형들의 각각의 두 점을 정의할 수있다. 

```cpp
for (int v = 1; v < this->ver_index.size(); v++) {
    for (int h = 1; h < this->hor_index.size(); h++) {
        Rectangle sub_rec(Points {this->ver_index[v - 1], this->hor_index[h - 1]}, Points {this->ver_index[v], this->hor_index[h]});
        this->_subR.push_back(sub_rec);
    }
}
```

# 더 알아볼 것

- 알게 된 사실: 벡터 컨테이너를 굳이 `resize()`해줄 필요 없으며, 초기화 한 사이즈대로 고정된다.
- 객체에서 멤버 변수에 접근할 때에 `this->`를 쓰지 않아도 되는 것으로 할고 있는데, 언제 생략하고 언제 생략하지 않는게 좋은가?
- 객체들을 넘겨주고 할 때에 값에 의한 복사인 것으로 알고 있는데 도대체 참조 연산자인 `&`가 마법처럼 *무엇을*해 주는건지 모르겠다. 예전에 강의 들을때 필기 해 둔거 같은데 찾아봐야 할 것 같다. 이거때문에 그런지 객체를 쓰면서도 값을 넘기는건지 레퍼런스를 넘기는건지 헷갈릴 때가 있다.

# 참조한 링크

- [\[C++\] vector(벡터) 정렬, 배열 정렬하기/Feel Coding](https://breakcoding.tistory.com/117)
- [C++ 고급 문법 테크닉 - C++ 객체 초기화\[5\]](https://ence2.github.io/2021/04/c-고급-문법-테크닉-c-객체-초기화5/)
- [Absolute Value/cplusplus](https://cplusplus.com/reference/cstdlib/abs/)
- [65 함수에서 구조체 매개변수 사용하기/C언어 코딩도장](https://dojang.io/mod/page/view.php?id=570)