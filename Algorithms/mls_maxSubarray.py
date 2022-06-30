# mls by danamic programming
# def maxSubarray(arr):
#     if len(arr) == 1:
#         return arr[0]
#     cache = [arr[0]]
#     for i in range(1, len(arr)):
#         cache.append(max(0, cache[-1]) + arr[i])
#     return max(cache)

def maxSubarray(arr):
    if len(arr) <= 1:
        return arr[0]
    half = len(arr) // 2
    left = maxSubarray(arr[:half])
    right = maxSubarray(arr[half:])

    lidx, ridx = half - 1, half
    lsum, rsum = arr[lidx], arr[ridx]
    lmax, rmax = arr[lidx], arr[ridx]

    for i in range(lidx - 1, -1, -1):
        lsum += arr[i]
        lmax = max(lmax, lsum)
    for i in range(ridx + 1, len(arr)):
        rsum += arr[i]
        rmax = max(rmax, rsum)

    center = lmax + rmax
    return max([left, right, center])


def main():
    size = int(input())
    for _ in range(size):
        arr = list(map(int, input().split()))
        print(maxSubarray(arr))


if __name__ == '__main__':
    main()
