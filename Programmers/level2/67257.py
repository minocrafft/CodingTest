"""
수식 최대화

link: https://school.programmers.co.kr/learn/courses/30/lessons/67257
type: 순열
"""


from itertools import permutations


def solution(expression):
    results = []
    for operator in permutations(["+", "-", "*"]):
        _most, _next, _last = operator
        temps = []

        for exp in expression.split(_last):
            temp = [f"({e})" for e in exp.split(_next)]
            temps.append(f"({_next.join(temp)})")

        results.append(abs(eval(_last.join(temps))))

    return max(results)


N = ["100-200*300-500+20", "50*6-3*2"]

for data in N:
    print(solution(data))
