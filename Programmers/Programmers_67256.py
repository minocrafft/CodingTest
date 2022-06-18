# Press Key pad
"""
    File Name: Programmers_67256.py
    File Contents: 키패드 누르기
    Programmed by Minho Kim 2022.06.18 (Sat)

    - 왼손은 *, 오른손은 #에서 시작
    - 상하좌우 4방향으로만 이동 가능, 한칸은 거리 1에 해당
    - 1,4,7은 왼손, 3,6,9는 오른손
    - 2,5,8,0은 현재 키패드에서 가까운 위치의 손으로 (동일하면 주 사용 손으로)
    - numbers, hand 매개변수 => 각 번호를 누른 손이 왼손인지 오른손인지 리스트로 반환
"""


def solution(numbers, hand):
    answer = ''
    fixed_KeyPad = {1: 'L', 4: 'L', 7: 'L', 3: 'R', 6: 'R', 9: 'R'}
    hand_type = {'left': 'L', 'right': 'R'}
    Key_Pad = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               ['*', 0, '#']]
    left_hand, right_hand = (3, 0), (3, 2)

    for n in numbers:
        coordinate = [(x, y) for x in range(len(Key_Pad)) for y in range(len(Key_Pad[0])) if Key_Pad[x][y] == n][0]
        if n in fixed_KeyPad.keys():
            answer += fixed_KeyPad[n]
            left_hand = coordinate if fixed_KeyPad[n] == 'L' else left_hand
            right_hand = coordinate if fixed_KeyPad[n] == 'R' else right_hand
        else:
            Left_distance = abs(left_hand[0] - coordinate[0]) + abs(left_hand[1] - coordinate[1])
            Right_distance = abs(right_hand[0] - coordinate[0]) + abs(right_hand[1] - coordinate[1])

            if Left_distance < Right_distance:
                answer += 'L'
                left_hand = coordinate
            elif Left_distance > Right_distance:
                answer += 'R'
                right_hand = coordinate
            else:
                answer += hand_type[hand]
                left_hand = coordinate if hand == 'left' else left_hand
                right_hand = coordinate if hand == 'right' else right_hand

    return answer