# Knumber
"""
    K번째 수

    - 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때
        k번째 수 구하기
"""

def solution(array, commands):
    answer = []
    for C in commands:
        L = list(array[C[0]-1:C[1]])
        L.sort()
        answer.append(L[C[2]-1])
    return answer

"""
# 다른 풀이
def solution(array, commands):
    answer = list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    return answer
"""