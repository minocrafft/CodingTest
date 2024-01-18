"""
우박수열 정적분

link: https://school.programmers.co.kr/learn/courses/30/lessons/134239
type: 구현
"""


def solution(k, ranges):
    def collatz(k):
        return k * 3 + 1 if k % 2 else k // 2

    def integral(y1, y2):
        return min(y1, y2) + abs(y2 - y1) * 0.5

    seq = [(0, k)]
    while k > 1:
        k = collatz(k)
        seq.append((len(seq), k))
    n = len(seq) - 1

    answer = []
    for a, b in ranges:
        if a > n + b:
            answer.append(-1)
        else:
            answer.append(
                sum([integral(seq[i][1], seq[i + 1][1]) for i in range(a, n + b)])
            )

    return answer


datas = [
    [5, [[0, 0], [0, -1], [2, -3], [3, -3]]],
    [3, [[0, 0], [1, -2], [3, -3]]],
]

for data in datas:
    print(solution(*data))
