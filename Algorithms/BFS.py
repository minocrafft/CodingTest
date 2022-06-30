from collections import deque

# 방향성 그래프
def create_adjacency_list(n, m):
    adjacency_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
    for adj in adjacency_list:
        adj.sort()
    return adjacency_list


def bfs_search(arr, start):
    queue = deque()
    dist = [-1] * len(arr)  # len(arr) = 4, case 1
    dist[start] = 0
    queue.append(start)  # start = 0
    sequence = [start]
    while queue:
        u = queue.popleft()  # u = 0
        for v in arr[u]:  # idx = 노드 번호, v = 연결된 노드들
            if dist[v] == -1:
                queue.append(v)
                dist[v] = dist[u] + 1
                sequence.append(v)
    return sequence


def main():
    size = int(input())
    for _ in range(size):
        N, M = map(int, input().split())
        adj_list = create_adjacency_list(N, M)
        print(*bfs_search(adj_list, 0))


if __name__ == '__main__':
    main()
