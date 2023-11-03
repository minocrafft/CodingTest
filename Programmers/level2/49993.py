"""
스킬트리

link: https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""


from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skills = deque(skill)
        for sk in skill_tree:
            if sk in skill and sk != skills.popleft():
                break
        else:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
