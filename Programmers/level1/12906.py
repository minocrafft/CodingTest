"""
같은 숫자는 싫어

link: https://programmers.co.kr/learn/courses/30/lessons/12906
"""


def solution(arr):
    answer = [arr[0]]
    for n in arr[1:]:
        if n != answer[-1]:
            answer.append(n)
    return answer
