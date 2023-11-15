"""
[1차] 프렌즈4블록

link: https://school.programmers.co.kr/learn/courses/30/lessons/17679
"""


def check(board, i, j):
    if board[i][j] == ".":
        return False
    elif board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
        return (i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)
    else:
        return False


def solution(m, n, board):
    answer = 0
    board = [list(b) for b in zip(*reversed(board))]

    blocks = True
    while blocks:
        blocks = set()
        for i in range(n - 1):
            for j in range(m - 1):
                results = check(board, i, j)
                if results:
                    blocks.update(results)

        newboard = [
            [board[i][j] for j in range(m) if (i, j) not in blocks] for i in range(n)
        ]

        for i, brd in enumerate(newboard):
            if len(brd) < m:
                newboard[i].extend(["."] * (m - len(brd)))

        board = newboard
        answer += len(blocks)

    return answer


M = [4, 6]
N = [5, 6]
BOARD = [
    ["CCBDE", "AAADE", "AAABF", "CCBBF"],
    ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"],
]

for data in zip(M, N, BOARD):
    print(solution(*data))
