from collections import deque


def fuel_check(g, gas_stations):
    fuel, fuel_cnt = g, 0
    distance = fuel
    gas_stations = deque(gas_stations)
    while len(gas_stations) >= 2:
        curr, next = gas_stations.popleft(), gas_stations.popleft()
        if curr + fuel < next:
            return -1
        if distance < next:
            fuel_cnt += 1
            distance = curr + fuel
        gas_stations.appendleft(next)

    return fuel_cnt


def main():
    size = int(input())
    for _ in range(size):
        G, L = map(int, input().split())
        gas_stations = list(map(int, input().split())) + [L]
        print(fuel_check(G, gas_stations))


if __name__ == '__main__':
    main()
