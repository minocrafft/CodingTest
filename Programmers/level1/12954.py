"""
x만큼 간격이 있는 n개의 숫자

link: https://programmers.co.kr/learn/courses/30/lessons/12954
"""


def solution(x, n):
    if x == 0:
        return [0] * n
    elif x > 0:
        return list(range(x, (x * n) + 1, x))
    else:
        return list(range(x, (x * n) - 1, x))
