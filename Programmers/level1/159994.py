"""
카드 뭉치

link: https://programmers.co.kr/learn/courses/30/lessons/159994
"""
from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for g in goal:
        if cards1 and g == cards1[0]:
            cards1.popleft()
        elif cards2 and g == cards2[0]:
            cards2.popleft()
        else:
            return "No"

    return "Yes"


cards1 = [
    ["i", "drink", "water"],
    ["i", "water", "drink"],
]

cards2 = [
    ["want", "to"],
    ["want", "to"],
]

goals = [
    ["i", "want", "to", "drink", "water"],
    ["i", "want", "to", "drink", "water"],
]


for c1, c2, g in zip(cards1, cards2, goals):
    print(solution(c1, c2, g))
