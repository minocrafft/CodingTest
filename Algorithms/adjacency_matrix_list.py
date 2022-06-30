# 가중치가 있는 방향성 그래프 - 인접 행렬
def create_adjacency_matrix(n, m):
    matrix = [[0]*n for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        matrix[u][v] = c
    return matrix


# 가중치가 없는 무방향 그래프 - 인접 리스트
def create_adjacency_list(n, m):
    adjacency_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list


def main():
    size = int(input())
    for _ in range(size):
        N, M = map(int, input().split())
        adj_list = create_adjacency_list(N, M)
        for lst in adj_list:
            print(*sorted(lst))


if __name__ == '__main__':
    main()
