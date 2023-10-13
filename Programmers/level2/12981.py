"""
영어 끝말잇기

link: https://school.programmers.co.kr/learn/courses/30/lessons/12981
"""


def solution(n, words):
    used = set([words[0]])
    count = [1] + [0] * (n - 1)
    prev = words[0]
    for i, word in enumerate(words[1:], 1):
        count[i % n] += 1

        if word in used or not word.startswith(prev[-1]):
            return [i % n + 1, count[i % n]]

        used.add(word)
        prev = word

    return [0, 0]


N = [3, 5, 2]
WORDS = [
    ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],
    [
        "hello",
        "observe",
        "effect",
        "take",
        "either",
        "recognize",
        "encourage",
        "ensure",
        "establish",
        "hang",
        "gather",
        "refer",
        "reference",
        "estimate",
        "executive",
    ],
    ["hello", "one", "even", "never", "now", "world", "draw"],
]


for n, words in zip(N, WORDS):
    print(solution(n, words))
