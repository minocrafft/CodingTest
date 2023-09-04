"""
바탕화면 정리

link: https://programmers.co.kr/learn/courses/30/lessons/161990
"""


def solution(wallpaper):
    """
    파일 index 찾아서 list에 담아서 x, y별로 최소 최대값 찾기
    """
    x, y = [], []
    for i, file in enumerate(wallpaper):
        for j, f in enumerate(file):
            if f == "#":
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x) + 1, max(y) + 1]


wallpapers = [
    [
        ".#...",
        "..#..",
        "...#.",
    ],
    [
        "..........",
        ".....#....",
        "......##..",
        "...##.....",
        "....#.....",
    ],
    [
        ".##...##.",
        "#..#.#..#",
        "#...#...#",
        ".#.....#.",
        "..#...#..",
        "...#.#...",
        "....#....",
    ],
    [
        "..",
        "#.",
    ],
]

for wallpaper in wallpapers:
    print(solution(wallpaper))
