# Compression of strings
"""
    File Name: Programmers_60057.py
    File Contents: 문자열 압축
    Programmed by Minho Kim 2022.06.14 (Tue)

    - 반복되는 문자열을 압축하기
    - s의 길이는 1 ~ 1000
    - s는 알파벳 소문자로만 이루어짐
    - 문자열은 제일 앞부터 잘라야함

    1. 반복되는 문자열 탐색
    2. 반복되는 문자열을 하나로 치환
    3. 현재 길이를 저장 후 길이가 제일 짧을 때까지 반복
"""


def solution(string):
    answer = []
    for step in range(1, int(len(string) / 2) + 2):
        split_string = [string[i:i + step] for i in range(0, len(string), step)]
        new_string = ''
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
