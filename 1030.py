def num(a):
    adult=0
    one=1
    two=0
    three=0
    for year in range(a-1):
        tmp=adult
        tnp=three
        adult+=three
        three=two
        two=one
        one=tmp+tnp
    return adult+one+two+three

while(True):
    try:
        a=int(input())
        if a!=0:
            print(num(a))
    except:
        break