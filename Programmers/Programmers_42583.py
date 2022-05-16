"""
    다리를 지나는 트럭

    - 트럭 여러대가 일차선 다리를 지날 때 걸리는 시간 구하기
    - 다리에는 트력이 최대 bridge_length대 올라갈 수 있으며, weight 이하의 무게만 견딜 수 있음
    - (다리에 완전히 오르지 않은 트럭 무게는 무시)
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
