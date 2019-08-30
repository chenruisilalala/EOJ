import numpy as np
n = 1000000

Prime = np.ones(n)
for j in range(2,int(n**0.5)):
    if Prime[j] == 1:
        for m in range(2,(n//j)):
            Prime[j*m] = 0


Prime[1] = 0

while(True):
    try:
        sum = 0
        a,b = map(int,input().strip().split())
        for k in range(a,b+1):
            sum+=Prime[k]
        print(sum)
    except:
        break