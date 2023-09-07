"""
개인정보 수집 유효기간

link: https://programmers.co.kr/learn/courses/30/lessons/150370
"""


def to_date(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    terms = {term.split()[0]: int(term.split()[1]) for term in terms}
    today = to_date(today)

    for i, privacy in enumerate(privacies, 1):
        _date, term = privacy.split()
        _date = to_date(_date)
        _date += terms[term] * 28 - 1

        if today > _date:
            answer.append(i)

    return answer


todays = [
    "2022.05.19",
    "2020.01.01",
]

terms = [
    ["A 6", "B 12", "C 3"],
    ["Z 3", "D 5"],
]

privacies = [
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"],
]

for today, term, privacy in zip(todays, terms, privacies):
    print(solution(today, term, privacy))
