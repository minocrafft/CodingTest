"""
폰켓몬

link: https://programmers.co.kr/learn/courses/30/lessons/1845
"""


def solution(nums):
    return min(len(nums) / 2, len(set(nums)))


nums = [3, 1, 2, 3]
nums2 = [3, 3, 3, 2, 2, 4]

print(solution(nums))
