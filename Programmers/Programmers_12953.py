"""
    - n개의 수의 최소공배수는 n개의 수들의 배수 중 공통이 되는 가장 작은 수
    - n개 숫자가 담긴 배열 arr에서 최소공배수 구하기

    # 소인수 분해 이용하기 - 공통인 인자 차출
"""

from collections import Counter
def PrimeFactorization(number):
    n = 2
    prime = []
    while n <= number:
        if number % n == 0:
            prime.append(n)
            number //= n
        else:
            n += 1
    return prime


def solution(arr):
    answer = 1
    num_dict = dict()
    for n in arr:
        for k, v in Counter(PrimeFactorization(n)).items():
            if k not in num_dict or num_dict[k] < v:
                num_dict[k] = v
    for k, v in num_dict.items():
        answer *= k ** v

    return answer

# 다른 풀이
"""
from math import gcd
def lcm(x, y):
   return x * y // gcd(x, y)

def solution(arr):
    answer = arr[0]
    for n in arr[1:]:
        answer = lcm(answer, n)

    return answer
"""