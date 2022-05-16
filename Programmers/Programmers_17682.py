"""
    다트 게임 - KAKAO BLIND RECRUITMENT

    점수 계산 로직 구현
    - 총 3번의 기회, 0 ~ 10점 사이 획득 가능
    - S, D, T 영역 당첨 시 차례로 1, 2, 3 제곱으로 계산
    - *(스타상): 바로 전에 얻은 점수 2배
    - #(아차상): 해당 점수 마이너스

    - 문자열 분리 => 점수 계산 => 총점 합산
"""

import re

def solution(dartResult):
    result = []
    # 정규식 컴파일, 1S, 2D*, 3T의 형태로 분할 계산
    r = re.compile("(\d+)([SDT])([*#])?")
    BONUS = {'S':"**1", 'D':"**2", 'T':"**3"}
    OPTION = {'*':"*2", '#':"*-1", '': "*1"}
    dart = r.findall(dartResult)

    for score, bonus, option in dart:
        # option이 *일 경우 이전 점수까지 2배로 계산
        if option == '*' and result != []:
            result[-1] *= 2
        # eval() 함수로 문자열 수식을 계산함
        result.append(eval(score + BONUS[bonus] + OPTION[option]))

    return sum(result)