# Lotto 최고 순위, 최저 순위
# win_nums와 비교 -> 맞으면 맞은 개수 count 증가
# 0일 경우 최고 순위는 (+ 0의 갯수 만큼), 최저 순위는 (- 0의 갯수)

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1] # 로또 순위를 list로 설정 cnt에 맞게 순위가 매겨짐.
    cnt = 0
    for n in lottos:
        if n in win_nums:
            cnt += 1    # 정답과 동일한 번호 갯수 추출
    
    return [rank[cnt + lottos.count(0)], rank[cnt]] # 0의 갯수만큼 더하면 최고 순위