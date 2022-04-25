# Printer
def solution(priorities, location):
    priorities = [(idx, pri) for idx, pri in enumerate(priorities)]
    pri = []
    
    while len(priorities) > 0:
        if priorities[0] == max(priorities, key=lambda x: x[1]):
            pri.append(priorities.pop(0))
        else:
            priorities.append(priorities.pop(0))

    for idx in range(len(pri)):
        if location == pri[idx][0]:
            return idx+1