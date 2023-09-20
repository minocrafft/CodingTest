"""
콜라 문제

link: https://programmers.co.kr/learn/courses/30/lessons/132267
"""


def solution(a, b, n):
    recalls = []
    while n >= a:
        recall = (n // a) * b
        n = recall + (n % a)
        recalls.append(recall)

    return sum(recalls)


a = [2, 3]
b = [1, 1]
n = [20, 20]

for _a, _b, _n in zip(a, b, n):
    print(solution(_a, _b, _n))
