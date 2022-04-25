# Carpet
def solution(brown, yellow):
    for row in range(1, brown + yellow):
        for col in range(1, row+1):
            if row*col == brown + yellow and (row-2)*(col-2) == yellow:
                return [row, col]