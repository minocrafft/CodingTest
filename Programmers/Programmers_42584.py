# Stock Price
def solution(prices):
    answer = []
    for idx, price in enumerate(prices):     
        t = 0
        for j in range(idx+1, len(prices)):
            t += 1
            if price > prices[j]:
                break
        answer.append(t)
    return answer