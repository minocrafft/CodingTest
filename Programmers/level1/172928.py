"""
공원 산책

link: https://programmers.co.kr/learn/courses/30/lessons/172928
"""


def move(park, pts, route):
    v, n = route.split()
    print(v, n)
    code = {
        "E": [0, 1],
        "W": [0, -1],
        "S": [1, 0],
        "N": [-1, 0],
    }

    _x, _y = 0, 0
    x, y = pts
    for _ in range(int(n)):
        _x, _y = x + code[v][0], y + code[v][1]
        try:
            if park[_x][_y] == "X":
                break
        except IndexError:
            return pts

    x += _x
    y += _y

    return x, y


def solution(park, routes):
    pts = (0, 0)
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                pts = (i, j)
                break

    for route in routes:
        print("pts: ", pts)
        pts = move(park, pts, route)

    return pts


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
