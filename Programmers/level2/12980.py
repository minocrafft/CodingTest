"""
점프와 순간 이동

link: https://school.programmers.co.kr/learn/courses/30/lessons/12980
"""


# other solution
# def solution(n):
#     return bin(n).count("1")


def solution(n):
    ans = 0
    while n > 0:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n //= 2

    return ans


N = [5, 6, 5000]

for n in N:
    print(solution(n))
