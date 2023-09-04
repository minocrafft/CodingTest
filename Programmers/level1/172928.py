"""
공원 산책

link: https://programmers.co.kr/learn/courses/30/lessons/172928
"""


def solution(park, routes):
    course = {
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0),
    }

    row, column = len(park), len(park[0])
    x, y = (0, 0)
    for i, p in enumerate(park):
        if "S" in p:
            x, y = i, p.index("S")
            break

    for route in routes:
        direction, n = route.split()
        dx, dy = course[direction]
        n = int(n)

        _x, _y = x, y
        for _ in range(n):
            if (
                0 <= _x + dx < row
                and 0 <= _y + dy < column
                and park[_x + dx][_y + dy] != "X"
            ):
                _x, _y = _x + dx, _y + dy
            else:
                _x, _y = x, y
                break

        x, y = _x, _y

    return [x, y]


parks = [
    ["SOO", "OOO", "OOO"],
    ["SOO", "OXX", "OOO"],
    ["OSO", "OOO", "OXO", "OOO"],
]

routes = [
    ["E 2", "S 2", "W 1"],
    ["E 2", "S 2", "W 1"],
    ["E 2", "S 3", "W 1"],
]

for park, route in zip(parks, routes):
    print(solution(park, route))
    print()
