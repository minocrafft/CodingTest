"""
    File Contents: 부족한 금액 계산하기
    Programmed by Minho Kim 2022.06.19 (sat)
"""
def solution(price, money, count):
    cost = sum([price * c for c in range(1, count + 1)])
    return cost - money if cost - money > 0 else 0