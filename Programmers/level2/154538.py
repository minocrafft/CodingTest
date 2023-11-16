"""
숫자 변환하기

link: https://school.programmers.co.kr/learn/courses/30/lessons/154538
"""


def solution(x, y, n):
    answer = 0
    _set = set([x])

    while _set:
        if y in _set:
            return answer

        new_set = set()
        for i in _set:
            for xi in (i + n, i * 2, i * 3):
                if xi <= y:
                    new_set.add(xi)

        _set = new_set
        answer += 1

    return -1


X = [10, 10, 2]
Y = [40, 40, 5]
N = [5, 30, 4]

for data in zip(X, Y, N):
    print(solution(*data))
