def num(a):
    i=[1]
    j=[1]
    if a==1:
        print("1\n")
    else:
        for line in range(a):
            i.append(1)
            j.append(1)
            for shit in range(len(i)):
                j[shit] = i[shit]
            i[0] = 1
            for row in range(1, line):
                i[row] = j[row] + j[row - 1]
            for num in range(len(i) - 2):
                print(i[num], end=" ")
            print('1')
        print()
    return 0

while(True):
    try:
        a=int(input())
        if a!=0:
            num(a)
    except:
        break