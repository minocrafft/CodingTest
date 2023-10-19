"""
할인 행사

link: https://school.programmers.co.kr/learn/courses/30/lessons/131127
"""


from collections import Counter


def solution(want, number, discount):
    count = 0
    want = Counter({w: n for w, n in zip(want, number)})

    if not (want - Counter(discount)):
        N = sum(number)
        for i in range(len(discount) - N + 1):
            products = Counter(discount[i : i + N])
            if want == products:
                count += 1

    return count


want = [["banana", "apple", "rice", "pork", "pot"], ["apple"]]
number = [[3, 2, 2, 2, 1], [10]]
discount = [
    [
        "chicken",
        "apple",
        "apple",
        "banana",
        "rice",
        "apple",
        "pork",
        "banana",
        "pork",
        "rice",
        "pot",
        "banana",
        "apple",
        "banana",
    ],
    [
        "banana",
        "banana",
        "banana",
        "banana",
        "banana",
        "banana",
        "banana",
        "banana",
        "banana",
        "banana",
    ],
]

for data in zip(want, number, discount):
    print(solution(*data))
