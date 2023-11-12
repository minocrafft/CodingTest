"""
롤케이크 자르기

link: https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""


from collections import Counter


def solution(topping):
    answer = 0
    kind1 = Counter(topping)
    kind2 = set()

    for top in topping:
        kind1[top] -= 1
        if kind1[top] == 0:
            del kind1[top]

        kind2.add(top)
        if len(kind1) == len(kind2):
            answer += 1

    return answer


topping = [
    [1, 2, 1, 3, 1, 4, 1, 2],
    [1, 2, 3, 1, 4],
]

for data in topping:
    print(solution(data))
