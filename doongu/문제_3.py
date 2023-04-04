# 정렬하니, 이분탐색 사용
def solution(citations):
    citations.sort(reverse = True)
    left, right = 0, len(citations)-1
    
    while left <= right:
        h = (left + right) // 2
        left, right = (left, h-1) if citations[h] <= h else (h + 1, right)
            
    return left