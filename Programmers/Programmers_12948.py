# Hide Phone number
def solution(phone_number):
    return ''.join(['*' for n in phone_number[:-4]] + [phone_number[-4:]])