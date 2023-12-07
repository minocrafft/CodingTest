"""
[PCCE 기출문제] 10번 / 데이터 분석

link: https://school.programmers.co.kr/learn/courses/30/lessons/250121
type: 구현
"""


def solution(data, ext, val_ext, sort_by):
    columns = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    newdata = []

    for _data in data:
        if _data[columns[ext]] < val_ext:
            newdata.append(_data)

    return sorted(newdata, key=lambda x: x[columns[sort_by]])


data = [[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]]
ext = ["date"]
val_ext = [20300501]
sort_by = ["remain"]


for _data in zip(data, ext, val_ext, sort_by):
    print(solution(*_data))
