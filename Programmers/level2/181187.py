"""
두 원 사이의 정수 쌍

link: https://programmers.co.kr/learn/courses/30/lessons/181187
"""
from math import sqrt, floor, ceil


def solution(r1, r2):
    count = 0
    for x in range(1, r2 + 1):
        max_y = floor(sqrt(r2**2 - x**2))
        min_y = ceil(sqrt(r1**2 - x**2)) if r1 > x else 0

        count += max_y - min_y + 1

    return count * 4


r1 = 2
r2 = 3
print(solution(r1, r2))
