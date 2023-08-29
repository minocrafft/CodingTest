"""
괄호 회전하기

link: https://programmers.co.kr/learn/courses/30/lessons/76502
"""


def check_bracket(string):
    stack = []
    for s in string:
        if s in ["[", "(", "{"]:
            stack.append(s)
        else:
            if not stack:
                return 0
            c = stack.pop()
            if (
                (s == "]" and c != "[")
                or (s == ")" and c != "(")
                or (s == "}" and c != "{")
            ):
                return 0

    return len(stack) == 0


def solution(s):
    right_cnt = 0
    for x in range(len(s)):
        s = s[1:] + s[0]
        right_cnt += check_bracket(s)

    return right_cnt
