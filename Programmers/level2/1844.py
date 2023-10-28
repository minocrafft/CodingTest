"""
게임 맵 최단거리

link: https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""


from collections import deque


def bfs(maps, start):
    N = len(maps)
    M = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([start])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                (nx == 0 and ny == 0)
                or nx < 0
                or ny < 0
                or nx >= N
                or ny >= M
                or maps[nx][ny] == 0
            ):
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[N - 1][M - 1]


def solution(maps):
    move = bfs(maps, (0, 0))
    if move == 1:
        return -1

    return move


maps = [
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ],
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ],
]

for data in maps:
    print(solution(data))
