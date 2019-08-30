while(True):
    try:
        b=[]
        a=int(input())
        for n in range(a):
            b.append(int(input()))
        b.sort()
        for i in b:
            print(i)
    except:
        break

