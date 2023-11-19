"""
2개 이하로 다른 비트

link: https://school.programmers.co.kr/learn/courses/30/lessons/77885
type: 진법 변환
"""


def solution(numbers):
    return [num + ((num ^ (num + 1)) >> 2) + 1 for num in numbers]


N = [[2, 7]]

for data in N:
    print(solution(data))
