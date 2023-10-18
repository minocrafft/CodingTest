"""
연속 부분 수열 합의 개수

link: https://school.programmers.co.kr/learn/courses/30/lessons/131701
"""


def solution(elements):
    L = len(elements)
    dp = elements.copy()
    elements *= 2
    subsets = set(dp)

    for i in range(1, L):
        for j in range(L):
            dp[j] += elements[j + i]
        subsets.update(dp)

    return len(subsets)


elements = [7, 9, 1, 1, 4]

print(solution(elements))
