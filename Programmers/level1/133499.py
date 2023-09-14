"""
옹알이 (2)

link: https://programmers.co.kr/learn/courses/30/lessons/133499 
"""


def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]

    count = 0
    for bab in babbling:
        for word in words:
            if word in bab and word * 2 not in bab:
                bab = bab.replace(word, " ")

        if bab.strip() == "":
            count += 1

    return count


babblings = [
    ["aya", "yee", "u", "maa"],
    ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"],
]

for babbling in babblings:
    print(solution(babbling))
