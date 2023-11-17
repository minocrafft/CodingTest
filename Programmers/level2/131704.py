"""
택배상자

link: https://school.programmers.co.kr/learn/courses/30/lessons/131704
type: stack
"""


def solution(order):
    idx = 0
    stack = []
    for num, _ in enumerate(order, 1):
        stack.append(num)

        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1

    return idx


order = [
    [4, 3, 1, 2, 5],
    [5, 4, 3, 2, 1],
]

for data in order:
    print(solution(data))
