"""
구명보트

link: https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""
from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    boat = 0

    while len(people) > 1:
        light, heavy = people.popleft(), people.pop()

        if light + heavy > limit:
            people.appendleft(light)

        boat += 1

    return boat + 1 if people else boat


PEOPLE = [[70, 50, 80, 50], [70, 80, 50]]
LIMIT = [100, 100]

for data in zip(PEOPLE, LIMIT):
    print(solution(*data))
