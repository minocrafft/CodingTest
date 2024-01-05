"""
시소 짝꿍

link: https://school.programmers.co.kr/learn/courses/30/lessons/152996
type: 구현
"""


from collections import defaultdict


def solution(weights):
    answer = 0
    possible = defaultdict(int)

    for w in weights:
        answer += (
            possible[w]
            + possible[w * 2]
            + possible[w / 2]
            + possible[w * 2 / 3]
            + possible[w * 3 / 2]
            + possible[w * 4 / 3]
            + possible[w * 3 / 4]
        )

        possible[w] += 1

    return answer


N = [[100, 180, 360, 100, 270]]

for data in N:
    print(solution(data))
