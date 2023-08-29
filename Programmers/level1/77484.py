"""
로또의 최고 순위와 최저 순위

link: https://programmers.co.kr/learn/courses/30/lessons/77484
"""


def solution(lottos, win_nums):
    grade = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    for n in lottos:
        if n in win_nums:
            cnt += 1

    return [grade[cnt + lottos.count(0)], grade[cnt]]
