"""
테이블 해시 함수

link: https://school.programmers.co.kr/learn/courses/30/lessons/147354
type: 구현
"""


from functools import reduce


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    hashes = []
    for i in range(row_begin, row_end + 1):
        hashes.append(sum([d % i for d in data[i - 1]]))

    return reduce(lambda x, y: x ^ y, hashes)


data = [[[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]]
col = [2]
begin = [2]
end = [3]

for _data in zip(data, col, begin, end):
    print(_data)
    print(solution(*_data))
