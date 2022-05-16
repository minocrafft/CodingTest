"""
    핸드폰 번호 가리기

    - 전화번호 뒷 4자리를 제외한 나머지 숫자를 전부 *로 변환
"""
def solution(phone_number):
    return ''.join(['*' for n in phone_number[:-4]] + [phone_number[-4:]])