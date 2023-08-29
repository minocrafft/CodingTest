"""
부족한 금액 계산하기

link: https://programmers.co.kr/learn/courses/30/lessons/82612
"""


def solution(price, money, count):
    cost = sum([price * c for c in range(1, count + 1)])
    return cost - money if cost - money > 0 else 0
