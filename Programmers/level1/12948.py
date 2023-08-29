"""
핸드폰 번호 가리기

link: https://programmers.co.kr/learn/courses/30/lessons/12948
"""


def solution(phone_number):
    return "".join(["*" for n in phone_number[:-4]] + [phone_number[-4:]])
