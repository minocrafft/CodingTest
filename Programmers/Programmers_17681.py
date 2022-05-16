# 비밀 지도 Secret Map

# 한변의 길이 n인 정사각혀으 공백 또는 #으로 칸 표현
# 두 지도 합쳐서 하나라도 벽 겹치면 벽
# 지도를 해독하기

# 이중 for loop
# arr의 원소 => 이진수 변환 후 or 연산

def mysolution(n, arr1, arr2):
    answer = []
    for array in zip(arr1, arr2):
        ans = ''
        b_num1 = bin(array[0])[2:].zfill(n)
        b_num2 = bin(array[1])[2:].zfill(n)
        for i in range(len(b_num1)):
            if b_num1[i] == '1' or b_num2[i] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)

    return answer

def solution(n, arr1, arr2):
    return [bin(arr1[i]|arr2[i]).zfill(n).replace('0', ' ').replace('1', '#') for i in range(n)]