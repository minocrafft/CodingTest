"""
최소직사각형

link: https://programmers.co.kr/learn/courses/30/lessons/86491
"""


def solution(sizes):
    width, height = [], []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))

    return max(width) * max(height)


sizes = [
    [[60, 50], [30, 70], [60, 30], [80, 40]],
    [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],
    [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]],
]

for size in sizes:
    print(solution(size))
