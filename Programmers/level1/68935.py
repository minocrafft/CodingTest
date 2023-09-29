"""
3진법 뒤집기

link: https://school.programmers.co.kr/learn/courses/30/lessons/68935
"""


def solution(n):
    result = ""

    while n > 0:
        result += str(n % 3)
        n //= 3

    return int(result, 3)


n = [45, 125]

for _n in n:
    print(solution(_n))
