"""
문자열 내 p와 y의 개수

link: https://programmers.co.kr/learn/courses/30/lessons/12916
"""


def solution(s):
    s = list(s.lower())
    return True if s.count("p") == s.count("y") else False
