"""
메뉴 리뉴얼

link: https://school.programmers.co.kr/learn/courses/30/lessons/72411
type: 조합
"""


from collections import Counter
from itertools import combinations


def solution(orders, course):
    menu = []

    for cors in course:
        combi = []
        for order in orders:
            combi += combinations(sorted(order), cors)

        combi = Counter(combi).most_common()
        menu += [key for key, value in combi if value >= 2 and value == combi[0][1]]

    return ["".join(m) for m in sorted(menu)]


orders = [
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
    ["XYZ", "XWY", "WXA"],
]


course = [[2, 3, 4], [2, 3, 5], [2, 3, 4]]


for data in zip(orders, course):
    print(solution(*data))
