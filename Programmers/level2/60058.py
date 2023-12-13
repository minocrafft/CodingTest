"""
괄호 변환

link: https://school.programmers.co.kr/learn/courses/30/lessons/60058
type: 재귀함수
"""


def reverse(bracket):
    r = {"(": ")", ")": "("}
    return "".join([r[b] for b in bracket])


def check_valanced(bracket):
    return bracket.count("(") == bracket.count(")")


def check_corrected(bracket):
    stack = []

    for brk in bracket:
        if stack and stack[-1] == "(" and brk == ")":
            stack.pop()
        else:
            stack.append(brk)

    return False if stack else True


def divide(bracket):
    newBracket = []
    for i, brk in enumerate(bracket, 1):
        newBracket.append(brk)

        if check_valanced(newBracket):
            return "".join(newBracket), bracket[i:]

    return "", "".join(bracket)


def convert_bracket(bracket):
    if bracket == "":
        return ""

    u, v = divide(bracket)

    if check_corrected(u):
        return "".join([u, convert_bracket(v)])
    else:
        return f"({convert_bracket(v)})" + reverse(u[1:-1])


def solution(p):
    return convert_bracket(p)


p = ["(()())()", ")(", "()))((()"]

for data in p:
    print(solution(data))
