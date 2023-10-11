"""
피보나치 수

link: https://school.programmers.co.kr/learn/courses/30/lessons/12945
"""


def solution(n):
    fibonacci = [0, 1]
    for _ in range(2, n + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci[-1] % 1234567


N = [3, 5]

for n in N:
    print(solution(n))
