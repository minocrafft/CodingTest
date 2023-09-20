"""
삼총사

link: https://school.programmers.co.kr/learn/courses/30/lessons/131705
"""

from itertools import combinations


def solution(number):
    combi = combinations(number, 3)
    combi = sum([sum(com) == 0 for com in combi])
    return combi


numbers = [
    [-2, 3, 0, 2, -5],
    [-3, -2, -1, 0, 1, 2, 3],
    [-1, 1, -1, 1],
]

for number in numbers:
    print(solution(number))
