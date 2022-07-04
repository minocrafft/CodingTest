"""
    File Contents: 크레인 인형뽑기 게임 - 2019 카카오 개발자 겨울 인턴십
    Programmed by Minho-Kim .2022.07.04 (Mon)

    - Stack 이용해서 구현
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