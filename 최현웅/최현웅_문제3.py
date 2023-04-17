import sys

input = sys.stdin.readline

# how to solve?

# 1. check_color 함수 : 분할된 정사각형이 모두 같은 색인지를 확인하는 함수, 그 함수가 true 를 반환하면 색깔에 따라 +1 을 해준다.
# 2. 분할된 정사각형이 모두 같은색이 아닌 경우, 계속 분할을 해준다.


def check_color(graph: list) -> int:
    if all(all(color == 1 for color in row) for row in graph):
        return 1
    elif all(all(color == 0 for color in row) for row in graph):
        return 0

    return -1


def solution(graph: list, size: int) -> None:
    global white, blue
    if check_color(graph) != -1:
        white, blue = (
            (white + 1, blue) if check_color(graph) == 0 else (white, blue + 1)
        )
        return

    devide_size = size // 2
    solution([row[:devide_size] for row in graph[:devide_size]], devide_size)
    solution([row[:devide_size] for row in graph[devide_size:size]], devide_size)
    solution([row[devide_size:size] for row in graph[:devide_size]], devide_size)
    solution([row[devide_size:size] for row in graph[devide_size:size]], devide_size)


if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    white = blue = 0

    solution(graph, N)
    print(white)
    print(blue)
