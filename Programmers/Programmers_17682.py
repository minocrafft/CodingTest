# KAKAO BLIND RECRUITMENT Level 1 Dart Game

# 점수 계산 로직 구현
# 총 3번의 기회, 0 ~ 10점 사이 획득 가능
# S, D, T 영역 당첨 시 차례로 1, 2, 3 제곱으로 계산
# *(스타상): 바로 전에 얻은 점수 2배, #(아차상) 해당 점수 마이너스

# 문자열 분리 => 점수 계산 => 총점 합산


import re

# 초기 구현 함수
"""
def calcScore(dartScore):
    result = []
    for s in dartScore:
        score = re.findall("\d+", s)
        bonus = re.findall("[SDT]", s)
        option = re.findall("[*#]", s)
        score = score[0]

        if 'S' in bonus: bonus = "**1"
        if 'D' in bonus: bonus = "**2"
        if 'T' in bonus: bonus = "**3"
        if '*' in option:
            option = "*2"
            if result != []: result[-1] *= 2
        if '#' in option: option = "*-1"
        if option == []: option = ''

        res = score + bonus + option
        result.append(eval(score + bonus + option))

    return sum(result)
        
def solution(dartResult):
    dartScore = re.findall("\d+\S\W?", dartResult)
    return calcScore(dartScore)
"""
#---------------------------------------------------------------#


# 개선된 함수
# calcScore() 함수를 간소화
def solution(dartResult):
    result = []
    r = re.compile("(\d+)([SDT])([*#])?")
    BONUS = {'S':"**1", 'D':"**2", 'T':"**3"}
    OPTION = {'*':"*2", '#':"*-1", '': "*1"}
    dart = r.findall(dartResult)

    for score, bonus, option in dart:
        if option == '*' and result != []:
            result[-1] *= 2
        result.append(eval(score + BONUS[bonus] + OPTION[option]))

    return sum(result)

dart = "1S2D*3T"
dart2 = "1D2S#10S"
dart4 = "1S*2T*3S"

print(solution(dart))