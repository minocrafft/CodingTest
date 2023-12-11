"""
[3차] 방금그곡

link: https://school.programmers.co.kr/learn/courses/30/lessons/17683
type:
"""


def fuse(code):
    target = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}
    for t in target:
        code = code.replace(t, target[t])

    return code


def parse(musicinfo):
    start, end, title, code = musicinfo.split(",")
    code = fuse(code)

    start = [int(st) for st in start.split(":")]
    end = [int(et) for et in end.split(":")]
    hour, minute = end[0] - start[0], end[1] - start[1]

    count = hour * 60 + minute
    if count > len(code):
        k, mod = divmod(count, len(code))
        code = code * k + code[:mod]
    else:
        code = code[:count]

    return title, code


def solution(m, musicinfos):
    m = fuse(m)
    for music in musicinfos:
        title, fullcode = parse(music)
        if m in fullcode:
            return title

    return "(None)"


m = [
    "ABCDEFG",
    "CC#BCC#BCC#BCC#B",
    "ABC",
]

musicinfos = [
    ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
    ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
    ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"],
]

for data in zip(m, musicinfos):
    print(solution(*data))
