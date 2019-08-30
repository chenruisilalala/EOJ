def gcm(a, b):
    assert a > 0 and b > 0
    while True:
        if a >= b:
            if a % b == 0:
                return b
            else:
                a, b = a - b, b
        else:
            a, b = b, a
def lcm(a, b):
    assert a > 0 and b > 0
    return int(a * b / gcm(a, b))
x,n=map(int, input().strip().split())
for i in range(2,n+1):
    print(int(lcm(x,i)/x))
