"""
콜라츠 추측

link: https://programmers.co.kr/learn/courses/30/lessons/12943
"""


def solution(num):
    cnt = 0
    while num != 1:
        cnt += 1
        num = num * 3 + 1 if num % 2 else num // 2
        if cnt > 500:
            return -1

    return cnt
