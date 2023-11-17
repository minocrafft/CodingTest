"""
땅따먹기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12913
type: DP
"""


def solution(land):
    for i in range(1, len(land)):
        l1, l2, l3, l4 = land[i - 1]
        land[i][0] += max(l2, l3, l4)
        land[i][1] += max(l1, l3, l4)
        land[i][2] += max(l1, l2, l4)
        land[i][3] += max(l1, l2, l3)

    return max(land[-1])


land = [
    [
        [1, 2, 3, 5],
        [5, 6, 7, 8],
        [4, 3, 2, 1],
    ]
]

for data in land:
    print(solution(data))
