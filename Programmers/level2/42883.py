"""
큰 수 만들기

link: https://school.programmers.co.kr/learn/courses/30/lessons/42883
type: Greedy
"""


def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    return "".join(stack if k == 0 else stack[:-k])


N = [
    "1924",
    "1231234",
    "4177252841",
]

k = [2, 3, 4]

for data in zip(N, k):
    print(solution(*data))
