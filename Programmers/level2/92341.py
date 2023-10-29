"""
주차 요금 계산

link: https://school.programmers.co.kr/learn/courses/30/lessons/92341
"""


import math
from datetime import timedelta
from collections import defaultdict


def solution(fees, records):
    answer = []
    base_time, base_fee, per_time, per_fee = fees
    timedict = defaultdict(float)
    recorddict = defaultdict(timedelta)

    for record in records:
        times, number, case = record.split()
        hour, minute = times.split(":")
        times = timedelta(hours=int(hour), minutes=int(minute))

        if case == "IN":
            recorddict[number] = times
            continue

        timedict[number] += (times - recorddict[number]).seconds / 60
        del recorddict[number]

    for number in recorddict:
        timedict[number] += (
            timedelta(hours=23, minutes=59) - recorddict[number]
        ).seconds / 60

    for number, elapsed in sorted(timedict.items(), key=lambda x: x[0]):
        fee = base_fee
        if elapsed > base_time:
            fee += math.ceil((elapsed - base_time) / per_time) * per_fee

        answer.append(fee)

    return answer


fees = [
    [180, 5000, 10, 600],
    [120, 0, 60, 591],
    [1, 461, 1, 10],
]

records = [
    [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT",
    ],
    [
        "16:00 3961 IN",
        "16:00 0202 IN",
        "18:00 3961 OUT",
        "18:00 0202 OUT",
        "23:58 3961 IN",
    ],
    ["00:00 1234 IN"],
]


for data in zip(fees, records):
    print(solution(*data))
