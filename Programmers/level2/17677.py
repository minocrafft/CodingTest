"""
[1차] 뉴스 클러스터링

link: https://programmers.co.kr/learn/courses/30/lessons/17677
"""
from collections import Counter


def make_charset(src):
    src = src.lower()
    charset = [src[i : i + 2] for i in range(len(src) - 1) if src[i : i + 2].isalpha()]
    return Counter(charset)


def solution(str1, str2):
    str1 = make_charset(str1)
    str2 = make_charset(str2)

    intersection = list((str1 & str2).elements())
    union = list((str1 | str2).elements())

    if (len(intersection) == 0) and (len(union) == 0):
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)
