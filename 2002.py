import math
while(True):
    try:
        a,b=map(int,input().strip().split())
        c=math.sqrt(a*a+b*b)
        print('%.3f' % c)
    except:
        break