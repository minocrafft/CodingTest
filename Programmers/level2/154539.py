"""
뒤에 있는 큰 수 찾기

link: https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number

        stack.append(idx)

    return answer


N = [
    [2, 3, 3, 5],
    [9, 1, 5, 3, 6, 2],
]

for data in N:
    print(solution(data))
