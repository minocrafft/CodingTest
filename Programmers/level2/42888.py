"""
오픈채팅방

link: https://programmers.co.kr/learn/courses/30/lessons/42888
"""


def solution(record):
    answer = []
    user_dictionary = dict()
    message = []
    for r in record:
        if len(r.split()) == 3:
            act, uid, name = r.split()
            user_dictionary[uid] = name
        else:
            act, uid = r.split()

        message.append((act, uid))

    for act, uid in message:
        if act == "Enter":
            answer.append(f"{user_dictionary[uid]}님이 들어왔습니다.")
        elif act == "Leave":
            answer.append(f"{user_dictionary[uid]}님이 나갔습니다.")

    return answer
