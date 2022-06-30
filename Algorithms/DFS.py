import sys
from time import time
sys.setrecursionlimit(1000000)

# 무방향성 그래프
def create_adjacency_list(n, m):
    adjacency_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    for adj in adjacency_list:
        adj.sort(reverse=True)
    return adjacency_list

# dfs for recursive function
def dfs_recursion(arr, u):  # arr = [[1, 3], [0,2,3], [1], [0,1]]
    visited = [False] * len(arr)  # len(arr) = 4, case 1
    visited[u] = True
    sequence = [u]
    for v in arr[u]:
        if not visited[v]:
            sequence.append(v)
            explore(arr, v, visited, sequence)
    return sequence

def explore(arr, v, visited, sequence):
    visited[v] = True
    for v in arr[v]:
        if not visited[v]:
            sequence.append(v)
            explore(arr, v, visited, sequence)


# dfs for stack
def dfs_stack(arr, u):
    stack = arr[u]
    visited = [False] * len(arr)  # len(arr) = 4, case 1
    visited[u] = True
    sequence = [u]
    while stack:
        v = stack.pop()
        if not visited[v]:
            sequence.append(v)
            visited[v] = True
            stack.extend(sorted(arr[v], reverse=True))
    return sequence


def main():
    size = int(input())
    for _ in range(size):
        N, M = map(int, input().split())
        adj_list = create_adjacency_list(N, M)
        print(adj_list)
        st = time()
        print("dfs_recursion: ", *dfs_recursion(adj_list, 0))
        print("dfs_recursion elapsed time: ", time() - st)

        st = time()
        print("dfs_stack: ", *dfs_stack(adj_list, 0))
        print("dfs_stack elapsed time: ", time() - st)


if __name__ == '__main__':
    main()
