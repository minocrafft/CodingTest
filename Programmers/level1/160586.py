"""
대충 만든 자판

link: https://programmers.co.kr/learn/courses/30/lessons/160586
"""
from itertools import chain


def solution(keymap, targets):
    answer = []
    keyset = set(chain(*[list(key) for key in keymap]))

    for target in targets:
        if len(set(target) - set(keyset)):
            answer.append(-1)
            continue

        count = 0
        for t in target:
            indice = [list(key).index(t) + 1 for key in keymap if t in list(key)]
            count += min(indice)

        answer.append(count)

    return answer


keymaps = [
    ["ABACD", "BCEFD"],
    ["AA"],
    ["AGZ", "BSSS"],
]
targets = [
    ["ABCD", "AABB"],
    ["B"],
    ["ASA", "BGZ"],
]


for keymap, target in zip(keymaps, targets):
    print(solution(keymap, target))
