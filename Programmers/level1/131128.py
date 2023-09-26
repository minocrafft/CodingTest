"""
숫자 짝꿍

link: https://school.programmers.co.kr/learn/courses/30/lessons/131128
"""

from collections import Counter


def solution(X, Y):
    X = Counter(X)
    Y = Counter(Y)
    pairs = list((X & Y).elements())
    if not pairs:
        return "-1"

    pairs = "".join(sorted(pairs, reverse=True))
    if pairs[0] == "0":
        return "0"

    return pairs


X = [
    "100",
    "100",
    "100",
    "12321",
    "5525",
]

Y = [
    "2345",
    "203045",
    "123450",
    "42531",
    "1255",
]

for x, y in zip(X, Y):
    print(solution(x, y))
