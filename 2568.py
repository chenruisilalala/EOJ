for i in range(int(input())):
    a,b=map(int,input().strip().split())
    print(len(list(map(eval,str(a+b)))))