"""
직사각형 별찍기

link: https://programmers.co.kr/learn/courses/30/lessons/12969
"""
a, b = map(int, input().split())
[print("*" * a) for _ in range(b)]
