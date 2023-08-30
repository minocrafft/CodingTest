"""
공원 산책

link: https://programmers.co.kr/learn/courses/30/lessons/172928
"""


def validate_move(maps, route):
    pass


def move(route):
    pass


def solution(park, routes):
    # maps = {i: k for i, k in enumerate(list("".join(park)))}
    width = len(park[0])
    maps = list("".join(park))
    print(maps)

    start = maps.index("S")

    result = []
    for route in routes:
        if validate_move(maps, route):
            result = move(route)

    return result


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
