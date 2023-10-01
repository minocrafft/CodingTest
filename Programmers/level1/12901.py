"""
2016년

link: https://school.programmers.co.kr/learn/courses/30/lessons/12901
"""
from datetime import datetime


def solution(a, b):
    weekday = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    base, target = datetime(2016, 1, 1), datetime(2016, a, b)
    return weekday[(target - base).days % len(weekday)]
