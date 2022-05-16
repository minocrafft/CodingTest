# Carpet
"""
    카페트

    - 카펫의 갈색 격자의 수와 노란색 격자의 수를 바탕으로 카펫의 가로,세로 크기 구하기
    - 가로 길이는 세로 길이와 같거나 더 큼
"""

def solution(brown, yellow):
    for row in range(1, brown + yellow):
        for col in range(1, row+1):
            if row*col == brown + yellow and (row-2)*(col-2) == yellow:
                return [row, col]