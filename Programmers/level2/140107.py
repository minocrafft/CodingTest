"""
점 찍기

link: https://school.programmers.co.kr/learn/courses/30/lessons/140107
type: 수식
"""


from math import sqrt


def solution(k, d):
    points = [sqrt(d**2 - y**2) // k + 1 for y in range(0, d + 1, k)]

    return sum(points)


N = [[2, 4], [1, 5]]

for data in N:
    print(solution(*data))
