#모든 요소가 같으면 멈춘다.
#요소가 하나라도 다르면 쪼갠다
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

result = []

def solution(x,y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                tmp = N//2
                solution(x, y, tmp)
                solution(x, y+tmp, tmp)
                solution(x+tmp, y+tmp, tmp)
                solution(x+tmp, y, tmp)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0, n)
print(result.count(0))
print(result.count(1))
