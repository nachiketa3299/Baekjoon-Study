# 풀이 시간 

- 12:17 ~ 12:50 33분
- 12:55 ~ 13:53 57분
- 총 90분

# 소스코드

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const bool isFirstAlpha (const string input) {
	return (input[0] >= 'A' && input[0] <= 'Z') ? true : false;
}
string searchAToI (vector<string> dict, string query) {
	for (int i = 0; i < dict.size(); i++) {
		if (dict[i] == query) {
			return to_string(i + 1);
		}
	}
}
string searchIToA (vector<string> dict, string query) {
	int target_index = stoi(query) - 1;
	return dict[target_index];
}

int main (void) {
	int N, M;
	// 1 <= N, M <= 100'000 , (N, M) in Natural Number
	cin >> N >> M;

	vector<string> dictionary (N);
	for (auto &e: dictionary) {
		// e is consists only of alphabets, and only first letter is uppercase.
		// 2 <= e.length() <= 20
		cin >> e;
	}
	vector<string> question_arr (M);
	for (auto &e: question_arr) {
		cin >> e;
	}

	vector<string> answer_arr (M);
	for (int i = 0; i < question_arr.size(); i++) {
		if (isFirstAlpha(question_arr[i])) {
			answer_arr.push_back(searchAToI(dictionary, question_arr[i]));
		} else {
			answer_arr.push_back(searchIToA(dictionary, question_arr[i]));
		}
	}

	for (auto e: answer_arr) {
		cout << e << endl;
	}

	return 0;
}
```
# 풀이 방법

- `M` 갯수대로 받은 데이터를 쿼리라고 칭한다.
- 이 쿼리는 `25`나 `Pickachu`와 같은 값을 갖는데, 어쨌든 모두 `string`형으로 저장한다.
- `N`크기의 딕셔너리를 만들고 쿼리의 원소별로 다음을 실행한다.
    1. 만약 쿼리가 알파벳으로 이루어져 있으면, 그러니까 해당 쿼리 문자열의 0번 인덱스가 `'A'`와 `'Z'`사이에 존재하는 경우
        - 딕셔너리 전체를 순회하면서 해당 쿼리 문자열과 일치하는 인덱스를 찾고, 해당 인덱스를 문자열로 바꿔 리턴한다.
    2. 만약 쿼리가 숫자로 이루어져 있으면. 그러니까 1. 이 아닌 경우 모두 이 경우이다.
        - 숫자로 이루어진 해당 쿼리를 정수로 바꾼 후, 딕셔너리의 인덱스 값으로 접근해 해당 딕셔너리 인덱스가 가지는 값(문자열)을 리턴한다.

# 어디서 문제가 있었던 것인가? (예상)

- 위 풀이 방법에서 1번 단계에서 시간 초과가 날 것 같은 강한 예감이 문제를 읽으면서 들었는데, 역시 시간 초과가 났다. 
- STL 검색인 `find`가 있는건 아는데, 시간복잡도에 대해 모른다. 더 공부할 필요가 있다.

# 기타

- Visual Studio Code가 오류가 있어서 Sublime Text로 바꾸다가, 빌드 시스템 구축이 너무 복잡해서 다시 Visual Studio Code로 돌아왔다. 이 과정에서 시간을 엄청나게 소요했다.

# 참조 링크 및 더 공부할 것

- C++ 타입 캐스팅 정리. 실무에서는 타입 캐스팅을 명시하는 것이 좋은가?
  - [C++ Type Conversion](https://www.programiz.com/cpp-programming/type-conversion)
- C++ 문자열과 숫자 간의 전환
  - [C++ string to int, int to string 형변환 하기/GODOG](https://godog.tistory.com/entry/C-string-to-int-int-to-string-형변환-하기)
  - [`std::stoi`, `std::stol`, `std::stoll`/cppreference.com](https://en.cppreference.com/w/cpp/string/basic_string/stol)
  - [Convert Int to String in C++ Using Different Methods/simplilearn](https://www.simplilearn.com/tutorials/cpp-tutorial/int-to-string-cpp)
- C++ 문자열이 숫자로 구성되어있는지 판단
    - [How to check if a C/C++ string is a int?/tutorialspoint](https://www.tutorialspoint.com/how-to-check-if-a-c-cplusplus-string-is-an-int)
- C++ `find`
  - [`std::find`/cplusplus](https://cplusplus.com/reference/algorithm/find/)
  - [Use find() and find_if() on a vector of strings - C++ STL Algorithm](http://www.java2s.com/example/cpp/stl-algorithm/use-find-and-findif-on-a-vector-of-strings.html)
- 배열 접근의 시간복잡도에 대해서
    - [배열의 시간 복잡도/do Developer](https://moonsu.tistory.com/58)
