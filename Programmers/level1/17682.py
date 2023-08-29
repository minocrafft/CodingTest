"""
[1차] 다트 게임

link: https://programmers.co.kr/learn/courses/30/lessons/17682
"""
import re


def solution(dartResult):
    result = []
    r = re.compile("(\d+)([SDT])([*#])?")
    BONUS = {"S": "**1", "D": "**2", "T": "**3"}
    OPTION = {"*": "*2", "#": "*-1", "": "*1"}
    dart = r.findall(dartResult)

    for score, bonus, option in dart:
        if option == "*" and result != []:
            result[-1] *= 2
        result.append(eval(score + BONUS[bonus] + OPTION[option]))

    return sum(result)
