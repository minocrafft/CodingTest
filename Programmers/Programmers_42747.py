# H-Index
"""
    H-Index

    - 어떤 과학자가 발표한 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고
        나머지 논문이 h번 이하 인용되었을때 h의 최댓값 구하기
"""

def solution(citations):
    answer = 0
    n = len(citations)
    for i in range(n-1,-1,-1):
        h = i+1
        cnt_use, cnt_not_use = 0, 0
        for j in citations:
            if j >= h:
                cnt_use += 1
        if cnt_use >= h:
            answer = h
            break
    return answer