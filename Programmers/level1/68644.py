"""
두 개 뽑아서 더하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/68644
"""
from itertools import combinations


def solution(numbers):
    return sorted(set([sum(combi) for combi in combinations(numbers, 2)]))


numbers = [
    [2, 1, 3, 4, 1],
    [5, 0, 2, 7],
]

for number in numbers:
    print(solution(number))
