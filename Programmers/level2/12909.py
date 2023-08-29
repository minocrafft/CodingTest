"""
올바른 괄호

link: https://programmers.co.kr/learn/courses/30/lessons/12909
"""


def solution(s):
    cnt = 0
    for c in s:
        if s[0] == ")" or cnt < 0:
            return False

        if c == "(":
            cnt += 1
        else:
            cnt -= 1

    if not cnt:
        return True

    return False
