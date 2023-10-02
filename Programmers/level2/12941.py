"""
최솟값 만들기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12941
"""


def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum([a * b for a, b in zip(A, B)])


A = [[1, 4, 2], [1, 2]]
B = [[5, 4, 4], [3, 4]]

for a, b in zip(A, B):
    print(solution(a, b))
