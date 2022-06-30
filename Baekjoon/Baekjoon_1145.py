# At least most of the multiple
if __name__ == '__main__':
    nList = list(map(int, input().split()))
    nList.sort()
    minNum = nList[0]

    while True:
        cnt = 0
        for n in nList:
            if minNum % n == 0:
                cnt += 1
        if cnt >= 3:
            print(minNum)
            break
        minNum += 1