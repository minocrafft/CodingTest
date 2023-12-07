"""
[PCCE 기출문제] 9번 / 이웃한 칸

link: https://school.programmers.co.kr/learn/courses/30/lessons/250125
type: 구현
"""


def solution(board, h, w):
    move = ((0, -1), (1, 0), (0, 1), (-1, 0))
    N = len(board)

    count = 0
    for dw, dh in move:
        if 0 <= h + dh < N and 0 <= w + dw < N and board[h][w] == board[h + dh][w + dw]:
            count += 1

    return count


board = [
    [
        ["blue", "red", "orange", "red"],
        ["red", "red", "blue", "orange"],
        ["blue", "orange", "red", "red"],
        ["orange", "orange", "red", "blue"],
    ],
    [
        ["yellow", "green", "blue"],
        ["blue", "green", "yellow"],
        ["yellow", "blue", "blue"],
    ],
]

h = [1, 0]
w = [1, 1]

for data in zip(board, h, w):
    print(solution(*data))
