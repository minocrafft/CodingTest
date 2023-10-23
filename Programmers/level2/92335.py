"""
K진수에서 소수 개수 구하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""


def convert(n, k):
    number = ""
    while n > 0:
        n, mod = divmod(n, k)
        number += str(mod)

    return number[::-1]


def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    number = convert(n, k).split("0")

    count = 0
    for _n in number:
        if _n and isPrime(int(_n)):
            count += 1

    return count


N = [437674, 110011]
K = [3, 10]

for data in zip(N, K):
    print(solution(*data))
