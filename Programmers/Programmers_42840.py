# mock test
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