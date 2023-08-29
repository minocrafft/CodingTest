"""
이상한 문자 만들기

link: https://programmers.co.kr/learn/courses/30/lessons/12930
"""


def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = "".join(
            [c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s[i])]
        )
    return " ".join(s)
