"""
약수의 합

link: https://programmers.co.kr/learn/courses/30/lessons/12928
"""
from math import sqrt


def prime(n):
    res = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            if i**2 != n:
                res.append(n // i)
    return res


def solution(n):
    return sum(prime(n))
