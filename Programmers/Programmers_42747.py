# H-Index
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