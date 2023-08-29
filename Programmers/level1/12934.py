"""
정수 제곱근 판별

link: https://programmers.co.kr/learn/courses/30/lessons/12934
"""
from math import sqrt


def solution(n):
    n = sqrt(n)
    return (n + 1) ** 2 if n.is_integer() else -1
