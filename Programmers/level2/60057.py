"""
문자열 압축

link: https://programmers.co.kr/learn/courses/30/lessons/60057
"""


def solution(string):
    answer = []
    for step in range(1, int(len(string) / 2) + 2):
        split_string = [string[i : i + step] for i in range(0, len(string), step)]
        new_string = ""
        cur_idx, cnt = 0, 0
        for idx in range(len(split_string)):
            if split_string[idx] == split_string[cur_idx]:
                cnt += 1
            else:
                if cnt > 1:
                    new_string += str(cnt) + split_string[cur_idx]
                else:
                    new_string += split_string[cur_idx]
                cur_idx, cnt = idx, 1
        if cnt > 1:
            new_string += str(cnt) + split_string[cur_idx]
        else:
            new_string += split_string[cur_idx]
        answer.append(new_string)

    return len(min(answer, key=lambda x: len(x)))
