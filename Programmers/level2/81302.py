"""
거리두기 확인하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/81302
type: 구현
"""


def check(array, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0

    for xi, yi in zip(dx, dy):
        if 0 <= x + xi < 5 and 0 <= y + yi < 5 and array[x + xi][y + yi] == "P":
            count += 1

    return count


def solution(places):
    answer = []

    for place in places:
        isPassed = True
        for i, plc in enumerate(place):
            for j, p in enumerate(plc):
                if p == "X":
                    continue

                target = 1 if p == "P" else 2
                if check(place, i, j) >= target:
                    isPassed = False
                    break

            if not isPassed:
                break

        answer.append(1 if isPassed else 0)

    return answer


N = [
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
]

for data in N:
    print(solution(data))
