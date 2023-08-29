"""
행렬의 덧셈

link: https://programmers.co.kr/learn/courses/30/lessons/12950
"""


def solution(arr1, arr2):
    return [[a1 + a2 for a1, a2 in zip(ar1, ar2)] for ar1, ar2 in zip(arr1, arr2)]
