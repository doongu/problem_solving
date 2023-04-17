#include <iostream>
#include <vector>
using namespace std;

vector<vector <int>> color;
vector<int> line;
int white_cnt = 0, blue_cnt = 0;

void input() {
	int N, num;
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> num;
			line.push_back(num);
		}
		color.push_back(line);
		line.clear();
	}
}

void divide(int x, int y, int N) {
	int cnt = 0;
	for (int i = y; i < y + N; i++) {
		for (int j = x; j < x + N; j++) {
			if (color[i][j] == 1) {
				cnt++;
			}
		}
	}

	if (cnt == 0)
		white_cnt++;
	else if (cnt == N * N)
		blue_cnt++;
	else {
		divide(x, y, N / 2);
		divide(x, y + N / 2, N / 2);
		divide(x + N / 2, y, N / 2);
		divide(x + N / 2, y + N / 2, N / 2);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	input();
	divide(0, 0, color.size());
	cout << white_cnt << "\n" << blue_cnt;
}