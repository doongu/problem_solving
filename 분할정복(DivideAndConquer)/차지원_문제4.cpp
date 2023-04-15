#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    sort(citations.begin(), citations.end());
    int start = 0;
    int end = citations.back();
    
    while (start <= end) {
        int mid = (start + end) / 2;
        int count = citations.end() - lower_bound(citations.begin(), citations.end(), mid);
        
        if (count >= mid) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    
    return end;
}
