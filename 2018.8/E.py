from math import sqrt
N = int(input())
M=[ p for p in   range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]
len=len(M)
print(len-1)
print(M[0],end='')
for i in range(len-1):
    print(' ',end='')
    print(M[i+1]-M[i],end='')