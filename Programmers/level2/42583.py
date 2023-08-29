"""
다리를 지나는 트럭

link: https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 큐 형태로 풀이.
    bridge = deque([0] * bridge_length)
    time, total_weight = 0, 0

    while bridge:
        time += 1
        w = bridge.popleft()

        if w != 0:
            total_weight -= w

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time
