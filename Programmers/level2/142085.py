"""
디펜스 게임

link: https://school.programmers.co.kr/learn/courses/30/lessons/142085
type: 힙
"""


import heapq


def solution(n, k, enemies):
    heap = []

    for i, enemy in enumerate(enemies):
        heapq.heappush(heap, enemy)
        if len(heap) > k:
            n -= heapq.heappop(heap)

        if n < 0:
            return i

    return len(enemies)


N = [
    (7, 3, [4, 2, 4, 5, 3, 3, 1]),
    (2, 4, [3, 3, 3, 3]),
]

for data in N:
    print(solution(*data))
