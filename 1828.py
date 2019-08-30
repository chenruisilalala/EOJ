while(True):
    try:
        a=int(input())
        if(a!=-1):
            print('{:02d}:{:02d}:{:02d}'.format(a//3600,(a%3600)//60,a%60))
    except:
        break