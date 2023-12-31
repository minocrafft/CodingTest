"""
마법의 엘리베이터

link: https://school.programmers.co.kr/learn/courses/30/lessons/148653
type: 구현
"""


def solution(storey):
    count = 0
    storey = [int(num) for num in str(storey)]

    while storey:
        floor = storey.pop()
        if floor < 5:
            count += floor
        elif floor == 5:
            count += floor
            if storey and storey[-1] >= 5:
                storey[-1] += 1
        else:
            count += 10 - floor
            if storey:
                storey[-1] += 1
            else:
                count += 1

    return count


N = [16, 2554]

for data in N:
    print(solution(data))
