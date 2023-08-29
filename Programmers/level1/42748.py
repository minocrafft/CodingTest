"""
K번째수

link: https://programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution(array, commands):
    answer = list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))

    return answer
