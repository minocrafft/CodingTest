"""
모음 사전

link: https://programmers.co.kr/learn/courses/30/lessons/84512
"""
from itertools import product, chain


def solution(word):
    words = ["A", "E", "I", "O", "U"]
    words = [product(words, repeat=i) for i in range(1, len(words) + 1)]
    words = sorted(["".join(word) for word in chain(*words)])
    return words.index(word) + 1


words = ["AAAAE", "AAAE", "I", "EIO"]

for word in words:
    print(solution(word))
