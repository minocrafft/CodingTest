"""
하노이의 탑

link: https://school.programmers.co.kr/learn/courses/30/lessons/12946
type: 재귀함수
"""


def hanoi(n, start, target, temp):
    if n == 1:
        return [[start, target]]

    return (
        hanoi(n - 1, start, temp, target)
        + [[start, target]]
        + hanoi(n - 1, temp, target, start)
    )


def solution(n):
    return hanoi(n, 1, 3, 2)


N = [2]

for data in N:
    print(solution(data))
