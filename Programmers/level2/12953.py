"""
N개의 최소공배수

link: https://programmers.co.kr/learn/courses/30/lessons/12953
"""
from collections import Counter


def gcd(number):
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
        for k, v in Counter(gcd(n)).items():
            if k not in num_dict or num_dict[k] < v:
                num_dict[k] = v
    for k, v in num_dict.items():
        answer *= k**v

    return answer
