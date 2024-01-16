"""
후보키

link: https://school.programmers.co.kr/learn/courses/30/lessons/42890
type: 구현
"""


from itertools import combinations


def solution(relation):
    candidate_keys = []

    def is_minimal(key: tuple) -> bool:
        for ckey in candidate_keys:
            if all(column in key for column in ckey):
                return False
        return True

    def is_unique(key: tuple) -> bool:
        distinct = set(tuple(row[idx] for idx in key) for row in relation)
        return len(distinct) == len(relation)

    degree = len(relation[0])
    for deg in range(degree):
        combination = combinations(range(degree), deg + 1)
        combination = filter(
            lambda key: is_minimal(key) and is_unique(key), combination
        )
        for key in combination:
            candidate_keys.append(key)

    return len(candidate_keys)


N = [
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
]

for data in N:
    print(solution(data))
