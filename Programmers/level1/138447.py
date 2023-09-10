"""
명예의 전당(1)

link: https://programmers.co.kr/learn/courses/30/lessons/138447
"""


def solution(k, score):
    answer = []
    honors = []
    for s in score:
        honors.append(s)
        honors.sort(reverse=True)
        if len(honors) > k:
            honors.pop()

        answer.append(honors[-1])

    return answer


k = [
    3,
    4,
]
score = [
    [10, 100, 20, 150, 1, 100, 200],
    [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000],
]

for _k, _score in zip(k, score):
    print(solution(_k, _score))
