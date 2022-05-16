# Function Develop
"""
    기능 개발

    - 각 기능은 진도가 100%일 때만 서비스에 반영
    - 뒤의 기능이 먼저 개발될 경우 앞의 기능과 함께 배포
    - 각 배포마다 몇개의 기능이 배포되는지 구하기
"""

import math

def solution(progresses, speeds):
    answer = []
    # 작업별 완료까지 남은 일수 계산, 소수점은 올림 연산으로 처리
    day = [math.ceil((100.0 - x)/y) for x, y in zip(progresses, speeds)]
    complete = 0

    # day 계산하여 배포일이 더 오래 걸리는 작업 전까지 완료 후 index 처리
    for i in range(len(day)):
        if day[i] > day[complete]:
            answer.append(i-complete)
            complete = i
    # 마지막 남은 작업 완료
    answer.append(len(day)-complete)
    
    return answer