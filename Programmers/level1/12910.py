"""
나누어 떨어지는 숫자 배열

link: https://programmers.co.kr/learn/courses/30/lessons/12910
"""


def solution(arr, divisor):
    answer = sorted([n for n in arr if not n % divisor])
    return answer if answer else [-1]
