# import bisect

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def main():
    size = int(input())
    for _ in range(size):
        arr = list(map(int, input().split()))
        target = list(map(int, input().split()))
        answer = [binary_search(arr, t) for t in target]
        print(*answer)


if __name__ == '__main__':
    main()
