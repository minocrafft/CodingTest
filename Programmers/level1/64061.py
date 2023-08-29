"""
크레인 인형뽑기 게임

link: https://programmers.co.kr/learn/courses/30/lessons/64061
"""


def solution(board, moves):
    answer = 0
    basket = []

    for m in moves:
        for b in board:
            if b[m - 1]:
                basket.append(b[m - 1])
                b[m - 1] = 0
                break

        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2

    return answer
