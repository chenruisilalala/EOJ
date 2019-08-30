def maopao(alist):
    n = len(alist)
    for j in range(n, 0, -1):
        count = 0
        for i in range(n - 1):
            if alist[i] < 0 and alist[i + 1] < 0:
                if -alist[i] > -alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    count += 1
            elif alist[i] < 0 and alist[i + 1] > 0:
                if - alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    count += 1
            elif alist[i] > 0 and alist[i + 1] < 0:
                if alist[i] > -alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    count += 1
            elif alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1

        if count == 0:
            return

while(True):
    try:
        a=int(input())
        num=input().strip().split()
        num=list(map(int,num))
        maopao(num)
        for each in range(len(num)-1):
            print(num[each],end=' ')
        print(num[-1])
    except:
        break