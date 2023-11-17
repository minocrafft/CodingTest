"""
피보나치 수

link: https://school.programmers.co.kr/learn/courses/30/lessons/12945
type: DP
"""


def solution(n):
    fibonacci = [0, 1]
    for _ in range(2, n + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci[-1] % 1234567


# solution 2 using generator
# def fibonacci(n):
#     fibo = [0, 1]
#     for i in range(2, n + 1):
#         fibo.append(fibo[-1] + fibo[-2])
#         yield fibo[-1]
#
#
# def solution(n):
#     return max(fibonacci(n)) % 1234567


N = [3, 5]

for n in N:
    print(solution(n))
