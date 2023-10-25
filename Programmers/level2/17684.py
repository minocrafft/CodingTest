"""
[3차] 압축

link: https://school.programmers.co.kr/learn/courses/30/lessons/17684
"""


from string import ascii_uppercase


def solution(msg):
    worddict = {word: i for i, word in enumerate(ascii_uppercase, 1)}
    answer = []

    while True:
        if msg in worddict:
            answer.append(worddict[msg])
            break

        for i, _ in enumerate(msg, 1):
            if msg[0:i] not in worddict:
                answer.append(worddict[msg[0 : i - 1]])
                worddict[msg[0:i]] = len(worddict) + 1
                msg = msg[i - 1 :]
                break

    return answer


MSG = [
    "KAKAO",
    "TOBEORNOTTOBEORTOBEORNOT",
    "ABABABABABABABAB",
]

for data in MSG:
    print(solution(data))
