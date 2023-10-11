"""
다음 큰 숫자

link: https://school.programmers.co.kr/learn/courses/30/lessons/12911
"""


def solution(n):
    target = n + 1
    while True:
        if bin(n).count("1") == bin(target).count("1"):
            return target

        target += 1


N = [78, 15]

for n in N:
    print(solution(n))
