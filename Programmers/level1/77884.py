"""
약수의 개수와 덧셈

link: https://programmers.co.kr/learn/courses/30/lessons/77884
"""
from math import sqrt


def prime(n):
    output = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            output.append(i)
            if i**2 != n:
                output.append(n // i)
    return output


def solution(left, right):
    return sum([n if len(prime(n)) % 2 == 0 else -n for n in range(left, right + 1)])
