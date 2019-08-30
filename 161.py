while(True):
    try:
        x=input()
        if(x[0]=='a' and x[2]=='b'):
            print('a+b')
        else:
            a=float(x[0])
            b=float(x[3])
            c=a+b
            if(int(c)==c):
                print(int(c))
            else:
                print(c)
    except:
        break