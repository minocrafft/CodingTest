# New ID Recommend
"""
    File Contents: 신규 아이디 추천
    Programmed by Minho Kim 2022.06.13 (Mon)

    - 아이디의 길이는 3~15
    - 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표만 사용 가능
    - 마침표는 처음과 끝, 또는 연속으로 사용 불가
    - new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정

    Preprocessing
    1단계 new_id의 모든 대문자를 소문자로 치환
    2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나로 치환
    4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
    6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
         만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복
"""

import re
def solution(new_id):
    new_id = re.sub('[^a-z0-9-_.]', '', new_id.lower())
    new_id = re.sub('[.]+', '.', new_id).strip('.')
    new_id = 'a' if new_id == '' else new_id[:15].strip('.')
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id
