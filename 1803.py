initn=int(input())
fish=list(map(int,input().strip().split()))
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    fish.append(b)
    for i in range(len(fish)-1):
        print(fish[i],end='')
    print(fish[-1])