#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int sumRange(const vector<vector<int>>& arr, int sx, int sy, int length) {
    int ex = sx + length - 1;
    int ey = sy + length - 1;
    return accumulate(arr.begin() + sx, arr.begin() + ex + 1, 0, [=](int a, const vector<int>& b) {
        return a + accumulate(b.begin() + sy, b.begin() + ey + 1, 0);
    });
}

void solution(int x, int y, int length, const vector<vector<int>>& board, vector<int>& ans) {
    if (length * length * board[x][y] == sumRange(board, x, y, length)) {
        ans[board[x][y]] += 1;
    } else {
        length /= 2;
        for (auto [dx, dy] : {make_pair(0, 0), make_pair(0, length), make_pair(length, 0), make_pair(length, length)}) {
            int nx = x + dx;
            int ny = y + dy;
            if (nx < board.size() && ny < board.size()) {
                solution(nx, ny, length, board, ans);
            }
        }
    }
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n));

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }
    vector<int> ans(2, 0);
    solution(0, 0, n, board, ans);
    cout << ans[0] << endl;
    cout << ans[1] << endl;
}
