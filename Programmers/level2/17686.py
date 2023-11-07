"""
[3차 파일명 정렬]

link: https://school.programmers.co.kr/learn/courses/30/lessons/17686
"""


import re


def solution(files):
    seperate = []
    for file in files:
        seperate.extend(re.findall("([^0-9]+)([0-9]+)(.*)", file))

    return [
        "".join(name)
        for name in sorted(seperate, key=lambda x: (x[0].lower(), int(x[1])))
    ]


files = [
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
]

for file in files:
    print(solution(file))
