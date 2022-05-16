"""
    전화번호 목록

    - 전화번호 목록 중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
"""

def solution(phone_book):
    phone_book.sort()
    for idx, phone in enumerate(phone_book):
        # out of range 오류 처리를 위한 구문
        if idx+1 == len(phone_book):
            break
        # number는 다음 번호가 됨
        number = phone_book[idx+1]
        # 현재 phone 번호가 다음 번호의 일부분과 동일할 시 False 반환
        if phone == number[:len(phone)]:
            return False
    return True


"""
# 다른 풀이
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True

"""