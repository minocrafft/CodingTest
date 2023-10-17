"""
귤 고르기

link: https://school.programmers.co.kr/learn/courses/30/lessons/138476
"""


from collections import Counter


def solution(k, tangerine):
    tangerine = Counter(tangerine)

    case, count = 0, 0
    for _, num in tangerine.most_common():
        case += 1
        count += num

        if count >= k:
            break

    return case


K = [6, 4, 2]
tangerines = [
    [1, 3, 2, 5, 4, 5, 2, 3],
    [1, 3, 2, 5, 4, 5, 2, 3],
    [1, 1, 1, 1, 2, 2, 2, 3],
]


for data in zip(K, tangerines):
    print(solution(*data))
