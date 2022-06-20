# rotation bracket
"""
    File Contents: 괄호 회전하기 - 월간 코드 챌린지 시즌2
    - (), [], {} 올바른 괄호
    - 괄호 문자열을 회전시켰을때 s가 올바른 괄호 문자열이 되게 하는 x의 개수
    - 0 <= x < s
"""

# Stack 이용해서 구현
def check_bracket(string):
    stack = []
    for s in string:
        if s in ['[', '(', '{']:
            stack.append(s)
        else:
            if not stack:
                return 0
            c = stack.pop()
            if (s == ']' and c != '[') or (s == ')' and c != '(') or (s == '}' and c != '{'):
                return 0

    return len(stack) == 0


def solution(s):
    right_cnt = 0
    for x in range(len(s)):
        s = s[1:] + s[0]
        right_cnt += check_bracket(s)

    return right_cnt