"""
쿼드압축 후 개수 세기

link: https://school.programmers.co.kr/learn/courses/30/lessons/68936
type: 재귀함수
"""


from collections import Counter


def quad_tree(arr):
    if all(all(x == 1 for x in row) for row in arr):
        return [1]
    elif all(all(x == 0 for x in row) for row in arr):
        return [0]
    else:
        half = len(arr) // 2
        return [
            *quad_tree([[x for x in row[:half]] for row in arr[:half]]),
            *quad_tree([[x for x in row[half:]] for row in arr[:half]]),
            *quad_tree([[x for x in row[:half]] for row in arr[half:]]),
            *quad_tree([[x for x in row[half:]] for row in arr[half:]]),
        ]


def solution(arr):
    count = Counter(quad_tree(arr))
    return [count[0], count[1]]


arr = [
    [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
    ],
]


for data in arr:
    print(solution(data))
