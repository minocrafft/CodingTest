"""
배달

link: https://school.programmers.co.kr/learn/courses/30/lessons/12978
type: 최단거리
"""


import heapq
from collections import defaultdict


def dijkstra(graph, start: int):
    visited = [False] * (len(graph) + 1)
    distance = {node: float("inf") for node in graph}
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        cur_cost, dst = heapq.heappop(hq)
        if not visited[dst]:
            visited[dst] = True
            for node, cost in graph[dst].items():
                dist = cur_cost + cost
                if dist < distance[node]:
                    distance[node] = dist
                    heapq.heappush(hq, (dist, node))

    return distance


def solution(N, road, K):
    graph = defaultdict(dict)

    for a, b, c in road:
        graph[a][b] = min(c, graph[a].get(b, float("inf")))
        graph[b][a] = min(c, graph[b].get(a, float("inf")))

    distance = dijkstra(graph, 1)

    return sum((1 for cost in distance.values() if cost <= K))


N = [5, 6]

road = [
    [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
    [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
]

K = [3, 4]


for data in zip(N, road, K):
    print(solution(*data))
