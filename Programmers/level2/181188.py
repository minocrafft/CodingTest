"""
요격 시스템

link: https://programmers.co.kr/learn/courses/30/lessons/181188 
"""


def solution(targets):
    answer, bound = 0, 0
    targets.sort()

    for s, e in targets:
        if bound > s:
            bound = min(bound, e)
        else:
            bound = e
            answer += 1

    return answer
