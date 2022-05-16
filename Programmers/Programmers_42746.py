# The Biggest Number
"""
    가장 큰 수

    - 정수를 이어붙여 가장 큰 수 만들기
    - 순서 재배치 가능
"""

def solution(numbers):
    answer = ''

    while(len(numbers) > 0):
        max_value = numbers[0]
        max_idx = 0

        for i in range(1, len(numbers)):
            if numbers[i] >= 100:
                if numbers[i]/100 > max_value:
                    max_idx = i
            elif numbers[i] >= 10:
                if numbers[i]/10 > max_value:
                    max_idx = i
            else:
                if numbers[i] > max_value:
                    max_idx = i
                    
        answer = answer + str(numbers.pop(max_idx))
        
    return answer

"""
# 다른 풀이
def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    L = list(map(str, numbers))
    L.sort(key= lambda x:x*3, reverse=True)
    return ''.join(L)
"""