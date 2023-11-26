"""
두 큐 합 같게 만들기

link: https://school.programmers.co.kr/learn/courses/30/lessons/118667
type: 투포인터
"""


def solution(queue1, queue2):
    Q = queue1 + queue2
    limit = len(Q)
    target = sum(Q) // 2
    curr = sum(queue1)
    i, j = 0, len(queue1)

    count = 0
    while i < limit and j < limit:
        if curr == target:
            return count
        elif curr < target:
            curr += Q[j]
            j += 1
        else:
            curr -= Q[i]
            i += 1

        count += 1

    return -1


Q1 = [
    [3, 2, 7, 2],
    [1, 2, 1, 2],
    [1, 1],
]
Q2 = [
    [4, 6, 5, 1],
    [1, 10, 1, 2],
    [1, 5],
]

for data in zip(Q1, Q2):
    print(solution(*data))
