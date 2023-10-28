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

        for xi, yi in zip(dx, dy):
            nx = x + xi
            ny = y + yi

            if (
                0 <= nx < N
                and 0 <= ny < M
                and maps[nx][ny] == 1
                and (nx != 0 or ny != 0)
            ):
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[-1][-1]


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
