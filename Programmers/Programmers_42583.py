# Bridge on Truck
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    total_weight = 0
    
    while bridge:
        time += 1
        w = bridge.popleft()
        
        if w == 0:
            pass
        else:
            total_weight -= w
            
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    
    return time