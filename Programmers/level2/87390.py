"""
n^2 배열 자르기

link: https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""


def solution(n, left, right):
    arr = []
    for i in range(left, right + 1):
        arr.append(max(divmod(i, n)) + 1)

    return arr


N = [3, 4]
left = [2, 7]
right = [5, 14]

for data in zip(N, left, right):
    print(solution(*data))
