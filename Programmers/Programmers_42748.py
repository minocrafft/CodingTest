# Knumber
def solution(array, commands):
    answer = list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    return answer


def My_solution(array, commands):
    answer = []
    for C in commands:
        L = list(array[C[0]-1:C[1]])
        L.sort()
        answer.append(L[C[2]-1])
    return answer