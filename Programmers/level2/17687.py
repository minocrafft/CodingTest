"""
[3차] n진수 게임

link: https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""


def convert(n, k):
    base = "0123456789ABCDEF"
    number = ""
    while n > 0:
        n, mod = divmod(n, k)
        number += base[mod]

    return number[::-1]


def solution(n, t, m, p):
    numbers = "0" + "".join(convert(i, n) for i in range(m * t))

    return numbers[p - 1 :: m][:t]


n = [2, 16, 16]
t = [4, 16, 16]
m = [2, 2, 2]
p = [1, 1, 2]


for data in zip(n, t, m, p):
    print(solution(*data))
