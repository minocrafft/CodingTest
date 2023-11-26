"""
삼각 달팽이

link: https://school.programmers.co.kr/learn/courses/30/lessons/68645
type: 구현
"""
from itertools import chain


def solution(n):
    triangle = [[0] * i for i in range(1, n + 1)]
    direction = (1, 0), (0, 1), (-1, -1)
    x, y, num = -1, 0, 1

    for i in range(n):
        for _ in range(i, n):
            dx, dy = direction[i % 3]
            x, y = x + dx, y + dy
            triangle[x][y] = num
            num += 1

    return list(chain(*triangle))


N = [4, 5, 6]

for data in N:
    print(solution(data))
