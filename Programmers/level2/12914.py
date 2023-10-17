"""
멀리 뛰기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12914
"""


def solution(n):
    if n <= 2:
        return n

    case = [1, 2]
    for _ in range(n - 2):
        case.append(case[-2] + case[-1])

    return case[-1] % 1234567


N = [4, 3]

for n in N:
    print(solution(n))
