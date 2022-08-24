'''
    File name: Programmers_77485.py
    File contents: 행렬 테두리 회전하기
    Programmed by Minho-Kim 2022.08.05.

    - 행렬의 테두리를 회전하는 함수 구현
    - querie마다 회전하며 Mtrx 업데이트 & 최소값 answer에 저장
'''
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
        rotated.rotate(1)
        answer.append(min(rotated))
        for (x, y), num in zip(sequences, rotated):
            mtrx[x][y] = num

    return answer