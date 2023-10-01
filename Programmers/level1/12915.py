"""
문자열 내 마음대로 정렬하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12915
"""


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


strings = [["sun", "bed", "car"], ["abce", "abcd", "cdx"]]
n = [1, 2]

for string, _n in zip(strings, n):
    print(solution(string, _n))
