"""
연속된 부분 수열의 합

link: https://school.programmers.co.kr/learn/courses/30/lessons/178870
"""


def solution(sequence, k):
    sequence.append(0)
    start, end, _k = 0, 0, sequence[0]
    i1, i2 = 0, float("inf")

    while end < len(sequence) - 1:
        if _k <= k:
            if _k == k and end - start < i2 - i1:
                i1, i2 = start, end
            end += 1
            _k += sequence[end]
        else:
            _k -= sequence[start]
            start += 1

    return [i1, i2]


sequences = [
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3, 4, 5],
    [2, 2, 2, 2, 2],
]

k = [7, 5, 6]

for sequence, _k in zip(sequences, k):
    print(solution(sequence, _k))
