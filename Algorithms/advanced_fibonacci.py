def fibo(n):
    if n in (0, 1):
        return n

    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    return f[n]


def main():
    size = int(input())
    for _ in range(size):
        n = int(input())
        print(fibo(n))


if __name__ == '__main__':
    main()
