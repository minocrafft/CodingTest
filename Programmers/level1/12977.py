"""
소수 만들기

link: https://programmers.co.kr/learn/courses/30/lessons/12977
"""
from math import sqrt
from itertools import combinations


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return 0
    return 1


def solution(nums):
    answer = 0
    comb_numbers = list(combinations(nums, 3))
    nums = list(map(sum, comb_numbers))
    for num in nums:
        answer += is_prime(num)

    return answer
