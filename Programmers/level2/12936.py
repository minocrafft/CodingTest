"""
줄 서는 방법

link: https://school.programmers.co.kr/learn/courses/30/lessons/12936
type: 재귀함수
"""

from math import factorial


def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))

    for i in range(n - 1, -1, -1):
        nfact = factorial(i)
        answer.append(numbers.pop((k - 1) // nfact))
        k %= nfact

    return answer


N = [3]
K = [5]

for data in zip(N, K):
    print(solution(*data))
