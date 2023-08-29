"""
신고 결과 받기

link: https://programmers.co.kr/learn/courses/30/lessons/92334
"""


def solution(id_list, report, k):
    report_board = {key: 0 for key in id_list}
    mail = {key: 0 for key in id_list}

    for r in set(report):
        user_id, reported_id = r.split()
        report_board[reported_id] += 1

    for r in set(report):
        user_id, reported_id = r.split()
        if report_board[reported_id] >= k:
            mail[user_id] += 1

    return list(mail.values())
