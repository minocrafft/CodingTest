"""
햄버거 만들기

link: https://programmers.co.kr/learn/courses/30/lessons/133502
"""


def solution(ingredient):
    cnt, stack = 0, []
    burgers = [1, 2, 3, 1]
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == burgers:
            cnt += 1
            for _ in range(4):
                stack.pop()

    return cnt
