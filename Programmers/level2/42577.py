"""
전화번호 목록

link: https://programmers.co.kr/learn/courses/30/lessons/42577
"""


def solution(phone_book):
    phone_book.sort()
    for idx, phone in enumerate(phone_book):
        if idx + 1 == len(phone_book):
            break
        number = phone_book[idx + 1]
        if phone == number[: len(phone)]:
            return False
    return True
