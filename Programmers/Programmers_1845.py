# Phoneketmon
from itertools import combinations
def solution(nums):
    return min(len(nums)/2, len(set(nums)))


def My_solution(nums):
    answer = 0
    set_num = set(nums)
    if len(nums)/2 >= len(set_num):
        return len(set_num)
    else:
        return len(nums)/2