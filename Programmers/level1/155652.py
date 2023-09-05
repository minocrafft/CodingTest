"""
둘만의 암호

link: https://programmers.co.kr/learn/courses/30/lessons/155652
"""
from string import ascii_lowercase


def solution(s, skip, index):
    answer = ""
    alphabet = sorted(set(ascii_lowercase) - set(skip))
    alphadict = {char: idx for idx, char in enumerate(alphabet)}

    for c in s:
        idx = (alphadict[c] + index) % len(alphabet)
        answer += alphabet[idx]

    return answer


s = "aukks"
skip = "wbqd"
index = 5

print(solution(s, skip, index))
