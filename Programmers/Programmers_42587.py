"""
    프린터
    
    - 중요도가 높은 문서 먼저 인쇄하는 프린터 구현
        1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        3. 그렇지 않으면 J를 인쇄합니다.
"""

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