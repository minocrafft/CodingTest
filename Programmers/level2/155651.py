"""
호텔 대실

link: https://school.programmers.co.kr/learn/courses/30/lessons/155651
type: 누적합, imos
"""


from collections import defaultdict


def solution(book_time):
    def convert_time(time):
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute

    booked = defaultdict(int)

    for book in book_time:
        start, end = map(convert_time, book)
        booked[start] += 1
        booked[end + 10] -= 1

    booked = sorted(booked.items())

    current, maxCount = 0, 0
    for book, count in booked:
        current += count
        maxCount = max(maxCount, current)

    return maxCount


book_time = [
    [
        ["15:00", "17:00"],
        ["16:40", "18:20"],
        ["14:20", "15:20"],
        ["14:10", "19:20"],
        ["18:20", "21:20"],
    ],
    [["09:10", "10:10"], ["10:20", "12:20"]],
    [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]],
]

for data in book_time:
    print(solution(data))
