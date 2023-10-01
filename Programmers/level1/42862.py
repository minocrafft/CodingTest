"""
체육복

link: https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""


def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    intersection = lost & reserve
    lost -= intersection
    reserve -= intersection

    for r in reserve:
        if r - 1 in lost:
            lost.discard(r - 1)
        elif r + 1 in lost:
            lost.discard(r + 1)

    return n - len(lost)


n = [5, 5, 3]
losts = [[2, 4], [2, 4], [3]]
reserves = [[1, 3, 5], [3], [1]]

for _n, lost, reserve in zip(n, losts, reserves):
    print(solution(_n, lost, reserve))
