temp=0
while(True):
    a=input()
    if(a=='THE END.'):
        break
    else:
        if(temp!=0):
            print('\n',end='')
        a=a.lower()
        mm = list(range(97,123))
        b = list(map(chr, mm))
        for letter in a:
            if letter not in b:
                a=a.replace(letter,'')
        len=len(a)
        half_len=int(len//2)
        if(int(len)%2==0):
            if(a[:half_len]==a[half_len:][::-1]):
                print('Yes',end='')
            else:
                print("No",end='')
        else:
            if (a[:half_len] == a[half_len+1:][::-1]):
                print('Yes',end='')
            else:
                print("No",end='')
    del a
    del len
    del half_len
    temp+=1