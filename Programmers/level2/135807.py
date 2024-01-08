"""
숫자 카드 나누기

link: https://school.programmers.co.kr/learn/courses/30/lessons/135807
type: 최대공약수
"""


from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    def checkGCD(array, value):
        return value if all(num % value for num in array) else 0

    gcdA, gcdB = reduce(gcd, arrayA), reduce(gcd, arrayB)

    valueA = checkGCD(arrayB, gcdA)
    valueB = checkGCD(arrayA, gcdB)

    return max(valueA, valueB)


arrayA = [[10, 17], [10, 20], [14, 35, 119]]
arrayB = [[5, 20], [5, 17], [18, 30, 102]]

for data in zip(arrayA, arrayB):
    print(solution(*data))
