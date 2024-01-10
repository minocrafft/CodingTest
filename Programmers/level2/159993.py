"""
미로 탈출

link: https://school.programmers.co.kr/learn/courses/30/lessons/159993
type: bfs
"""


from collections import deque


def bfs(maps, start, target):
    R, C = len(maps), len(maps[0])
    mx = (-1, 1, 0, 0)
    my = (0, 0, -1, 1)

    cost = [[0] * C for _ in range(R)]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(mx, my):
            if (
                0 <= x + dx < R
                and 0 <= y + dy < C
                and maps[x + dx][y + dy] != "X"
                and cost[x + dx][y + dy] == 0
                and (x + dx, y + dy) != start
            ):
                cost[x + dx][y + dy] = cost[x][y] + 1
                queue.append((x + dx, y + dy))

    return cost[target[0]][target[1]]


def solution(maps):
    board = {m: (i, j) for i, mp in enumerate(maps) for j, m in enumerate(mp)}

    s2l = bfs(maps, board["S"], board["L"])
    if s2l == 0:
        return -1

    l2e = bfs(maps, board["L"], board["E"])
    if l2e == 0:
        return -1

    return s2l + l2e


maps = [
    ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"],
    ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"],
]

for data in maps:
    print(solution(data))
