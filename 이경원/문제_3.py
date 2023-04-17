def solution(citations):
    citations.sort(reverse = True)
    number = [i for i in range(1, len(citations) + 1)]
    H_idx = 0
    
    for i in range(len(number)):
        # 모든 논문에 대해서 인용된 횟수가 논문의 갯수보다 많은 경우
        if citations[-1] > number[-1]: return number[-1]
        # 모든 논문의 인용 횟수가 0인 경우
        if citations[0] == 0: return 0
    
        if citations[i] >= number[i]:
            H_idx = number[i]
        else: 
            H_idx = number[i-1]
            return H_idx
    return H_idx