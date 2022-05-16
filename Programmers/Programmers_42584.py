# Stock Price
"""
    주식 가격
    
    - 초 단위로 기록된 주식가격 배열이 있을 때, 가격이 떨어지지 않은 기간 구하기
"""

def solution(prices):
    answer = []
    # 2차원 배열로 풀었음
    for idx, price in enumerate(prices):     
        t = 0
        # idx번째 다음 가격부터 for loop로 계산
        for j in range(idx+1, len(prices)):
            # 시간초 증가
            t += 1
            # 대상 price와 다음 번째 price와 비교하여 현재 price가 더 크면 값이 떨어진 것이므로 break
            if price > prices[j]:
                break
        answer.append(t)
    return answer