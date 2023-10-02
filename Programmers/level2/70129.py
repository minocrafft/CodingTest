"""
이진 변환 반복하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""


def solution(s):
    count, zeros = 0, 0

    while s != "1":
        ones = s.count("1")
        zeros += len(s) - ones
        s = bin(ones).replace("0b", "")

        count += 1

    return [count, zeros]


S = [
    "110010101001",
    "01110",
    "1111111",
]

for s in S:
    print(solution(s))
