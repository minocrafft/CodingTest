"""
키패드 누르기

link: https://programmers.co.kr/learn/courses/30/lessons/67256
"""


def solution(numbers, hand):
    answer = ""
    fixed_KeyPad = {1: "L", 4: "L", 7: "L", 3: "R", 6: "R", 9: "R"}
    hand_type = {"left": "L", "right": "R"}
    Key_Pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    left_hand, right_hand = (3, 0), (3, 2)

    for n in numbers:
        coordinate = [
            (x, y)
            for x in range(len(Key_Pad))
            for y in range(len(Key_Pad[0]))
            if Key_Pad[x][y] == n
        ][0]
        if n in fixed_KeyPad.keys():
            answer += fixed_KeyPad[n]
            left_hand = coordinate if fixed_KeyPad[n] == "L" else left_hand
            right_hand = coordinate if fixed_KeyPad[n] == "R" else right_hand
        else:
            Left_distance = abs(left_hand[0] - coordinate[0]) + abs(
                left_hand[1] - coordinate[1]
            )
            Right_distance = abs(right_hand[0] - coordinate[0]) + abs(
                right_hand[1] - coordinate[1]
            )

            if Left_distance < Right_distance:
                answer += "L"
                left_hand = coordinate
            elif Left_distance > Right_distance:
                answer += "R"
                right_hand = coordinate
            else:
                answer += hand_type[hand]
                left_hand = coordinate if hand == "left" else left_hand
                right_hand = coordinate if hand == "right" else right_hand

    return answer
