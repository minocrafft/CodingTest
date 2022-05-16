"""
카카오 블라인드 채용 문제 - 신고 결과 받기

각 유저는 한 번에 한명의 유저만 신고 가능
    - 동일한 유저에 대한 신고는 1회로 간주
k번 이상 신고된 유저 게시판 정지, 해당 유저를 신고한 유저에게 메일 발송
"""

def solution(id_list, report, k):
    # 신고 횟수 기록과 메일 발송 횟수 기록을 위한 딕셔너리 선언
    reportBoard = {key: 0 for key in id_list}
    mail = {key: 0 for key in id_list}

    # report 당한 횟수 계산해서 저장
    for r in set(report):
        userID, reportedID = r.split()
        reportBoard[reportedID] += 1

    # report 당한 횟수가 k 이상인 유저에 대해 메일 보낸 사람의 메일 받는 횟수 계산
    for r in set(report):
        userID, reportedID = r.split()
        if reportBoard[reportedID] >= k:
            mail[userID] += 1

    return list(mail.values())