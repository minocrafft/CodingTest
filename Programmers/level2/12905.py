"""
가장 큰 정사각형 찾기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12905
type: DP
"""


def solution(board):
    row = len(board) + 1
    col = len(board[0]) + 1
    dp = [[0] * col for _ in range(row)]
    square = 0

    for i in range(1, row):
        for j in range(1, col):
            if board[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                square = max(dp[i][j], square)

    return square**2


N = [
    [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]],
    [[0, 0, 1, 1], [1, 1, 1, 1]],
]

for data in N:
    print(solution(data))
