# how to solve?

# 1. 정렬, 이분탐색

# * why 이분탐색?
# citations = [2, 5, 7, 11, 20] 인 경우
# a. start, end = 0, 20 이고, mid = 10 이다.

# b. 10 번 이상 인용된 논문이 10개 이상이 있어야 하는데, 이 조건을 만족하지 못한다. 10번 이상 인용된 논문은 2개이다.
# b-1. 이 말은, citations 배열에서 10보다 더 큰 값. 즉, 10의 오른쪽에 대해서는 볼 필요가 없다는 뜻이다.
# b-2. 10번 이상 인용된 논문이 10개 이상이 없는데, 10번 보다 더 많이 인용된 논문이 10개 보다 더 많은 경우는 발생하지 않으므로.

# c. 따라서, start, end = 0, 9 이고, mid = 4 인 경우로 탐색을 해본다.
# c-1. 4번 이상 인용된 논문의 수는 4개 이상이고, 나머지 논문들은 모두 4번 이하로 인용됐다. 이 경우 4가 최댓값임을 알 수 있다.

# keyword = h 의 최댓값을 찾는다 즉, h 를 작은 값 부터 키워간다.


def solution(citations):
    answer = 0
    citations.sort()

    start, end = 0, citations[-1]

    while start <= end:
        mid = (start + end) // 2
        idx = 0

        for i in range(len(citations)):
            if citations[i] >= mid:
                idx = i
                break

        if len(citations) - idx >= mid:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer
