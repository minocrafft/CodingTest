# Find prime numbers
"""
    소수 찾기

    - 수가 적힌 종이 조각을 붙여 소수 만들기
    - 종이 조각으로 만들 수 있는 소수가 몇개인지 반환
"""

# 에라토스테네스의 체 검색해보기
import math
from itertools import permutations

# 소수 판별
def is_prime_number(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    set_number = set()
    for i in range(len(numbers)):
        set_number |= set(map(int, map(''.join, permutations(list(numbers), i+1))))

    for num in set_number:
        if is_prime_number(num):
            answer.append(num)
    
    return len(answer)