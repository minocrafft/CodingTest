"""
H-Index

link: https://programmers.co.kr/learn/courses/30/lessons/42747
"""


def solution(citations):
    citations.sort(reverse=True)  # 6, 5, 3, 1, 0
    n = len(citations)
    L = []

    for i in range(n):
        cnt = 0
        h = citations[i]

        for j in citations:
            if h <= j:
                cnt += 1

            if cnt >= h:
                L.append(cnt)
                break

    return max(L)
