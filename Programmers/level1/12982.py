"""
예산

link: https://school.programmers.co.kr/learn/courses/30/lessons/12982
"""


def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while budget >= 0 and d:
        deposit = d.pop()

        if budget - deposit >= 0:
            budget -= deposit
            answer += 1

    return answer
