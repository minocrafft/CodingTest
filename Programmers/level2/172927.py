"""
광물 캐기

link: https://school.programmers.co.kr/learn/courses/30/lessons/172927
type: 구현
"""


def solution(picks, minerals):
    minerals = [minerals[i : i + 5] for i in range(0, len(minerals), 5)][: sum(picks)]
    minerals.sort(
        key=lambda m: (m.count("diamond"), m.count("iron"), m.count("stone")),
        reverse=True,
    )
    fatigues = {
        "diamond": {"diamond": 1, "iron": 1, "stone": 1},
        "iron": {"diamond": 5, "iron": 1, "stone": 1},
        "stone": {"diamond": 25, "iron": 5, "stone": 1},
    }

    answer = 0
    target = "diamond"
    for mineral in minerals:
        for i, pick in enumerate(("diamond", "iron", "stone")):
            if picks[i] > 0:
                picks[i] -= 1
                target = pick
                break

        for m in mineral:
            answer += fatigues[target][m]

    return answer


N = [
    [
        [1, 3, 2],
        ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
    ],
    [
        [0, 1, 1],
        [
            "diamond",
            "diamond",
            "diamond",
            "diamond",
            "diamond",
            "iron",
            "iron",
            "iron",
            "iron",
            "iron",
            "diamond",
        ],
    ],
]

for data in N:
    print(solution(*data))
