"""
덧칠하기

link: https://programmers.co.kr/learn/courses/30/lessons/161989
"""


def solution(n, m, section):
    prev, count = section[0], 1
    for sec in section:
        if sec - prev >= m:
            prev = sec
            count += 1

    return count


ns = [8, 5, 4]
ms = [4, 4, 1]
sections = [
    [2, 3, 6],
    [1, 3],
    [1, 2, 3, 4],
]

for n, m, section in zip(ns, ms, sections):
    print(solution(n, m, section))
