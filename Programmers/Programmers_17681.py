"""
    비밀 지도 Secret Map - 카카오 블라인드 채용

    - 한변의 길이가 n인 정사각형의 공백 또는 #으로 칸 표현
    - 두 지도 합쳐서 하나라도 벽이 겹치면 벽으로 생각함
    - 지도를 해독하기

    *문제 해결 아이디어*
    - Binary로 변환 후 OR 연산으로 벽을 계산
    - 0과 1을 벽과 공백으로 대체함
"""

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        wall = bin(arr1[i]|arr2[i])[2:].zfill(n)
        answer.append(wall.replace('0', ' ').replace('1', '#'))

    return answer