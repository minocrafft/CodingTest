# unfinished athlete
"""
    완주하지 못한 선수

    - 단 한명의 선수를 제외하고 모든 선수가 마라톤 완주
    - 완주하지 못한 선수 찾기
"""
from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()
    # 정렬 후 참여자와 완주자가 다른 지점이 있으면 그 사람이 완주를 못한 사람이 됨.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 못찾은 경우는 마지막 사람이 남은 완주 못한 사람
    return participant[-1]


"""
# 다른 풀이
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
"""