"""
소수 찾기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12921
"""


def get_primes(number):
    arr = [False, False] + [True] * (number - 1)

    for i in range(2, int(number**0.5) + 1):
        if arr[i]:
            for j in range(i * 2, number + 1, i):
                arr[j] = False

    return arr


def solution(n):
    return sum(get_primes(n))


n = [10, 5]

for _n in n:
    print(solution(_n))
