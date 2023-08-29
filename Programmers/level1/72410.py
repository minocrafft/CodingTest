"""
신규 아이디 추천

link: https://programmers.co.kr/learn/courses/30/lessons/72410
"""
import re


def solution(new_id):
    new_id = re.sub("[^a-z0-9-_.]", "", new_id.lower())
    new_id = re.sub("[.]+", ".", new_id).strip(".")
    new_id = "a" if new_id == "" else new_id[:15].strip(".")
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id
