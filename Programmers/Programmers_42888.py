"""
    카카오 블라인드 채용 문제 - 오픈채팅방

    - 각 유저는 유저 아이디로 구분
    - 다른 닉네임으로 입장시에도 이전 메세지의 이름이 바뀌어야함.
    - 퇴장하지 않고 방에서 바로 닉네임 변경도 가능함.
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
        if act == 'Enter':
            answer.append(f"{user_dictionary[uid]}님이 들어왔습니다.")
        elif act == "Leave":
            answer.append(f"{user_dictionary[uid]}님이 나갔습니다.")

    return answer