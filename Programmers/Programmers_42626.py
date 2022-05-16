"""
    더 맵게

    - 모든 음식의 스코빌 지수를 K 이상으로 만들기
    - 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    - 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞음
"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        answer += 1

    return answer