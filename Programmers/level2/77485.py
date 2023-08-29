"""
행렬 테두리 회전하기

link: https://programmers.co.kr/learn/courses/30/lessons/77485
"""
from collections import deque


def find_sequence(x1, y1, x2, y2):
    sequence = list(map(lambda y: (x1, y), range(y1, y2 + 1)))
    sequence.extend(list(map(lambda x: (x, y2), range(x1 + 1, x2 + 1))))
    sequence.extend(list(map(lambda y: (x2, y), range(y2 - 1, y1 - 1, -1))))
    sequence.extend(list(map(lambda x: (x, y1), range(x2 - 1, x1, -1))))
    return sequence


def solution(rows, columns, queries):
    answer = []
    mtrx = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    for querie in queries:
        sequences = find_sequence(*map(lambda x: x - 1, querie))
        rotated = deque([mtrx[x][y] for (x, y) in sequences])
        answer.append(min(rotated))
        rotated.rotate(1)
        for (x, y), num in zip(sequences, rotated):
            mtrx[x][y] = num

    return answer
