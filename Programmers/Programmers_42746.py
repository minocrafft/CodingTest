# The Biggest Number
def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    L = list(map(str, numbers))
    L.sort(key= lambda x:x*3, reverse=True)
    return ''.join(L)