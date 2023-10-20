"""
행렬의 곱셈

link: https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""


def solution(arr1, arr2):
    return [[sum(a * b for a, b in zip(A, B)) for B in zip(*arr2)] for A in arr1]


arr1 = [
    [[1, 4], [3, 2], [4, 1]],
    [[2, 3, 2], [4, 2, 4], [3, 1, 4]],
]

arr2 = [
    [[3, 3], [3, 3]],
    [[5, 4, 3], [2, 4, 1], [3, 1, 1]],
]

for data in zip(arr1, arr2):
    print(solution(*data))
