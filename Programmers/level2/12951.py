"""
JadenCase 문자열 만들기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12951
"""


def solution(s):
    s = list(s.title())
    for i, _s in enumerate(s[:-1], 1):
        if _s.isdigit():
            s[i] = s[i].lower()

    return "".join(s)


s = ["3people unFollowed me", "for the last week"]

for _s in s:
    print(solution(_s))
