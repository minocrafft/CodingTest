"""
숫자의 표현

link: https://school.programmers.co.kr/learn/courses/30/lessons/12924
"""


def solution(n):
    answer = 1
    half = n // 2 + 1

    for i in range(1, half):
        total = 0
        for j in range(i, half + 1):
            total += j
            if total == n:
                answer += 1
                break
            elif total > n:
                break

    return answer


print(solution(15))
