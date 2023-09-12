"""
과일 장수

link: https://programmers.co.kr/learn/courses/30/lessons/135808
"""


def solution(k, m, score):
    score.sort(reverse=True)
    score = [score[i : i + m] for i in range(0, len(score), m)]
    score = [min(s) * m for s in score if len(s) == m]

    return sum(score)
