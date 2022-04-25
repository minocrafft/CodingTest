# Find prime numbers
import math
from itertools import permutations

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