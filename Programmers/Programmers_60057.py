# Compression of strings
"""
    File Contents:문자열 압축
    Programmed by Minho Kim 2022.06.14 (Tue)

    - 반복되는 문자열을 압축하기
    - s의 길이는 1 ~ 1000
    - s는 알파벳 소문자로만 이루어짐
    - 문자열은 제일 앞부터 잘라야함

    1. 반복되는 문자열 탐색
    2. 반복되는 문자열을 하나로 치환
    3. 현재 길이를 저장 후 길이가 제일 짧을 때까지 반복
"""

from collections import Counter
import re


def solution(string):
    print(string)
    answer = []
    for step in range(1, len(string)):
        split_string = [string[i:i + step] for i in range(0, len(string), step)]
        print(f"new_string is {split_string}")
        new_string = ''
        i, j, cnt = 0, 0, 0
        for s in range(len(split_string)):
            if split_string[s] == split_string[i]:
                cnt += 1
            else:
                if cnt == 1:
                    new_string += split_string[i]
                    continue
                new_string += str(cnt) + split_string[i]
                cnt = 1
                i = s
        answer.append(new_string)

    print(answer)


        # counter_string = Counter(split_string)
        # for k in counter_string.keys():
        #     print(f"Key for Counter_string: {k}")
        #     if k in split_string:
        #         new_string = re.sub(f'{k}+', f'{k}', string)
        #         print(f"new_string: {new_string}")
        # new_string = re.replace(f'{Counter_string}')

        # print(f"{dir(re.__doc__)}")


s = "aabbaccc"
solution(s)