"""
    모의고사

    - 수포자 삼인방의 문제 풀이
    - 각각의 찍는 방식에 따라 정답을 가장 많이 맞힌 사람 찾기
    - 동률일 경우 오름차순으로 정렬 후 출력
"""

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]

    for idx,answer in enumerate(answers):
        if pattern1[idx%5] == answer:
            score[0] += 1
        if pattern2[idx%8] == answer:
            score[1] += 1
        if pattern3[idx%10] == answer:
            score[2] += 1

    answer = []
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)

    return answer