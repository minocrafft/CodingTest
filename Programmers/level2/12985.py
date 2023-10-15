"""
예상 대진표

link: https://school.programmers.co.kr/learn/courses/30/lessons/12985
"""

# others
# def solution(n, a, b):
#     return ((a - 1) ^ (b - 1)).bit_length()


def solution(n, a, b):
    answer = 1
    a, b = sorted([a, b])
    while not (b - a == 1 and a % 2 and not b % 2):
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        answer += 1

    return answer


N = 8
A = 4
B = 7

print(solution(N, A, B))
