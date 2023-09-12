"""
푸드 파이트 대회

link: https://programmers.co.kr/learn/courses/30/lessons/134240
"""


def solution(food):
    answer = ""
    food = {i: f for i, f in enumerate(food[1:], 1)}
    for k, v in food.items():
        if v >= 2:
            answer += str(k) * (v // 2)

    answer += "0" + answer[::-1]

    return answer
