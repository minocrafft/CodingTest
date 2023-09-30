"""
시저 암호

link:
"""
from string import ascii_letters

LETTERS = list(ascii_letters)


def solution(s, n):
    answer = ""

    for _s in s:
        if _s.isupper():
            answer += LETTERS[(LETTERS.index(_s) - 26 + n) % 26 + 26]
        elif _s.islower():
            answer += LETTERS[(LETTERS.index(_s) + n) % 26]
        else:
            answer += " "

    return answer


S = ["AB", "z", "a B z"]
N = [1, 1, 4]


for s, n in zip(S, N):
    print(solution(s, n))
