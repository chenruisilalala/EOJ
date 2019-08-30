# -*-coding:utf-8 -*-
def change(n):
    m = []
    while (n // 2 != 0):
        m.append(n % 2)
        n = n // 2
    m.append(n % 2)
    return m


a = int(input())
for i in range(a):
    x,y = map(int, input().strip().split())
    m=change(x)
    n=change(y)
    tmp=0
    a=len(m)
    b=len(n)
    le=abs(a-b)
    c=a
    if(a>b):
        for j in range(le):
            n.append(0)
        c=a
    elif(a<b):
        for j in range(le):
            m.append(0)
        c=b
    for k in range(c):
        if(m[k]!=n[k]):
            tmp+=1
    print(tmp)