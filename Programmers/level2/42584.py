"""
주식가격

link: https://programmers.co.kr/learn/courses/30/lessons/42584
"""


def solution(prices):
    answer = []
    for idx in range(len(prices)):
        t = 0
        for j in range(idx + 1, len(prices)):
            t += 1
            if prices[idx] > prices[j]:
                break
        answer.append(t)

    return answer
