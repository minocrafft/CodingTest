"""
리코쳇 로봇

link: https://school.programmers.co.kr/learn/courses/30/lessons/169199
type: bfs
"""


from collections import deque


def bfs(board, target):
    def move(x, y, dx, dy):
        while 0 <= x + dx < R and 0 <= y + dy < C and board[x + dx][y + dy] != "D":
            x += dx
            y += dy
        return x, y

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    gx, gy = target["G"]
    R, C = len(board), len(board[0])
    visited = [[0 if b == "R" else -1 for b in brd] for brd in board]

    queue = deque([target["R"]])
    while queue:
        x, y = queue.popleft()
        for direction in zip(dx, dy):
            nx, ny = move(x, y, *direction)
            if visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited[gx][gy]


def solution(board):
    target = {b: (i, j) for i, brd in enumerate(board) for j, b in enumerate(brd)}

    return bfs(board, target)


board = [
    ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."],
    [".D.R", "....", ".G..", "...D"],
]

for data in board:
    print(solution(data))
