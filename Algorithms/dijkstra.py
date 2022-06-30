import heapq

def create_adjacency_list_weight(n, m):
    adjacency_list = dict()
    for _ in range(m):
        u, v, c = map(int, input().split())
        if adjacency_list.get(u):
            adjacency_list[u][v] = c
        else:
            adjacency_list[u] = {v: c}
    for i in range(n):
        if not adjacency_list.get(i):
            adjacency_list[i] = dict()

    return adjacency_list


def dijkstra(graph, start):
    visited = [False] * len(graph)  # len(arr) = 4, case 1
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cur_cost, dst = heapq.heappop(hq)
        if not visited[dst]:
            visited[dst] = True
            for node, cost in graph[dst].items():
                distance = cur_cost + cost
                if distance < dist[node]:
                    dist[node] = distance
                    heapq.heappush(hq, (distance, node))
    return dist


def main():
    size = int(input())
    for _ in range(size):
        N, M = map(int, input().split())
        adj_list = create_adjacency_list_weight(N, M)
        dijkstra_cost = dijkstra(adj_list, 0)
        print(dijkstra_cost[N-1]) if dijkstra_cost[N-1] < float('inf') else print(-1)


if __name__ == '__main__':
    main()
