"""
무인도 여행

link: https://school.programmers.co.kr/learn/courses/30/lessons/154540
type: DFS or Linked list
"""


def linked_node(ground):
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    result = []

    while ground:
        start = ground.pop()
        stack, linked = [start], [start]

        while stack:
            i, j = stack.pop()

            for x, y in zip(dx, dy):
                if (i + x, j + y) in ground:
                    stack.append((i + x, j + y))
                    linked.append((i + x, j + y))
                    ground.remove((i + x, j + y))

        result.append(linked)

    return result


def solution(maps):
    ground = []
    for i, _map in enumerate(maps):
        for j, m in enumerate(_map):
            if m != "X":
                ground.append((i, j))

    ground = linked_node(ground)
    for i, grd in enumerate(ground):
        ground[i] = sum([int(maps[i][j]) for i, j in grd])

    return sorted(ground) if ground else [-1]


maps = [["X591X", "X1X5X", "X231X", "1XXX1"], ["XXX", "XXX", "XXX"]]

for data in maps:
    print(solution(data))
