"""
124 나라의 숫자

link: https://programmers.co.kr/learn/courses/30/lessons/12899
type: 진법 변환
"""


def solution(n):
    answer = ""
    while n > 0:
        n, mod = divmod(n - 1, 3)
        answer += "124"[mod]
    return answer[::-1]


N = [1, 2, 3, 4]

for data in N:
    print(solution(data))
