"""
방문 길이

link: https://school.programmers.co.kr/learn/courses/30/lessons/49994
"""


def solution(dirs):
    move = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    visited = set()

    x, y = 0, 0
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.update({(x, y, nx, ny), (nx, ny, x, y)})
            x, y = nx, ny

    return len(visited) // 2


DIRS = [
    "ULURRDLLU",
    "LULLLLLLU",
]

for data in DIRS:
    print(solution(data))
