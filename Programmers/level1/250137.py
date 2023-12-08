"""
[PCCP 기출문제] 1번

link: https://school.programmers.co.kr/learn/courses/30/lessons/250137
type: 구현
"""


def solution(bandage, health, attacks):
    hp = health
    current = 1
    casting, recovery, advantage = bandage

    for dt, damage in attacks:
        elapsed = dt - current
        hp += elapsed * recovery + (elapsed // casting) * advantage
        if hp > health:
            hp = health

        hp -= damage
        if hp <= 0:
            return -1

        current = dt + 1

    return hp


bandage = [[5, 1, 5], [3, 2, 7], [4, 2, 7], [1, 1, 1]]


health = [30, 20, 20, 5]


attacks = [
    [[2, 10], [9, 15], [10, 5], [11, 5]],
    [[1, 15], [5, 16], [8, 6]],
    [[1, 15], [5, 16], [8, 6]],
    [[1, 2], [3, 2]],
]


for data in zip(bandage, health, attacks):
    print(solution(*data))
