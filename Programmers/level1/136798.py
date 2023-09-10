"""
기사단원의 무기

link: https://programmers.co.kr/learn/courses/30/lessons/136798
"""


def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i**2 != n:
                divisors.append(n // i)

    return sorted(divisors)


def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        atk = len(get_divisors(n))
        if atk > limit:
            atk = power

        answer += atk

    return answer


numbers = [5, 10]
limits = [3, 3]
powers = [2, 2]

for number, limit, power in zip(numbers, limits, powers):
    print(solution(number, limit, power))
