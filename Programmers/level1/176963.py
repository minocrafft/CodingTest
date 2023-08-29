"""
추억 점수

link: https://programmers.co.kr/learn/courses/30/lessons/176963
"""
from collections import defaultdict


def solution(name, yearning, photo):
    score = defaultdict(int)
    for n, year in zip(name, yearning):
        score[n] = year

    scores = []
    for p in photo:
        scores.append(sum([score[n] for n in p]))

    return scores


names = [
    ["may", "kein", "kain", "radi"],
    ["kali", "mari", "don"],
    ["may", "kein", "kain", "radi"],
]

yearnings = [
    [5, 10, 1, 3],
    [11, 1, 55],
    [5, 10, 1, 3],
]

photos = [
    [
        ["may", "kein", "kain", "radi"],
        ["may", "kein", "brin", "deny"],
        ["kon", "kain", "may", "coni"],
    ],
    [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]],
    [["may"], ["kein", "deny", "may"], ["kon", "coni"]],
]

for name, year, photo in zip(names, yearnings, photos):
    print(solution(name, year, photo))
