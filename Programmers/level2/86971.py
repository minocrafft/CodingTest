"""
전력망을 둘로 나누기

link: https://programmers.co.kr/learn/courses/30/lessons/86971
"""
from collections import deque


def create_graph(wires, n):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    return graph


def bfs(graph, start):
    queue = deque([start])
    visited = [False] * len(graph)
    visited[start] = True

    while queue:
        item = queue.popleft()

        for i in graph[item]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return sum(visited)


def solution(n, wires):
    answer = n
    graph = create_graph(wires, n)

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        answer = min(abs(bfs(graph, v1) - bfs(graph, v2)), answer)

        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer


n = [9, 4, 7]
wires = [
    [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]],
    [[1, 2], [2, 3], [3, 4]],
    [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]],
]

for _n, _wires in zip(n, wires):
    print(solution(_n, _wires))
