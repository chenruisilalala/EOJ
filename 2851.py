def fun(n, m):
    return(n + m)
def reverse(n):
    print(n)
    print(int(str(n)[::-1]))
    return(int(str(n)[::-1]))

n = int(input())
i = 0
m = reverse(n)
while(m != n):
    n = fun(m, n)
    m = reverse(n)
    i += 1
print('%d %d'% (i,n))