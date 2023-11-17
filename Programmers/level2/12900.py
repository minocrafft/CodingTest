"""
2 x n 타일링

link: https://school.programmers.co.kr/learn/courses/30/lessons/12900
type: DP
"""


def solution(n):
    dp1, dp2 = 1, 2
    for _ in range(n - 1):
        dp1, dp2 = dp2, (dp1 + dp2) % 1_000_000_007

    return dp1


N = [4]

for data in N:
    print(solution(data))
