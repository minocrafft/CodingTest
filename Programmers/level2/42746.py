"""
가장 큰 수

link: https://programmers.co.kr/learn/courses/30/lessons/42746
"""


def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    L = list(map(str, numbers))
    L.sort(key=lambda x: x * 3, reverse=True)
    return "".join(L)
