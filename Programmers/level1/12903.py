"""
가운데 글자 가져오기

link: https://programmers.co.kr/learn/courses/30/lessons/12903
"""


def solution(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 == 1 else s[mid - 1 : mid + 1]
