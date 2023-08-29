"""
음양 더하기

link: https://programmers.co.kr/learn/courses/30/lessons/76501
"""


def solution(absolutes, signs):
    for i, sign in enumerate(signs):
        if not sign:
            absolutes[i] *= -1
    return sum(absolutes)
