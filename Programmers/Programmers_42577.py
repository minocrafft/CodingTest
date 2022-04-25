# List of Phonebook
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


def My_solution(phone_book):
    phone_book.sort()
    for idx, phone in enumerate(phone_book):
        if idx+1 == len(phone_book):
            break
        number = phone_book[idx+1]
        if phone == number[:len(phone)]:
            return False
    return True