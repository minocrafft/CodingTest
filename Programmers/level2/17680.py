"""
[1차] 캐시

link: https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""


from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    elapsed = 0

    for city in cities:
        city = city.lower()

        if city in cache:
            elapsed += 1
            cache.remove(city)
        else:
            elapsed += 5

        cache.append(city)

    return elapsed


cacheSize = [3, 3, 2, 5, 2, 0]
cities = [
    [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
    ],
    ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
    [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "SanFrancisco",
        "Seoul",
        "Rome",
        "Paris",
        "Jeju",
        "NewYork",
        "Rome",
    ],
    [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "SanFrancisco",
        "Seoul",
        "Rome",
        "Paris",
        "Jeju",
        "NewYork",
        "Rome",
    ],
    ["Jeju", "Pangyo", "NewYork", "newyork"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
]


for data in zip(cacheSize, cities):
    print(solution(*data))
