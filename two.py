a=int(input())
def change(a):
    ini=a
    num=0
    for i in range(8):
        wei=ini%10
        ini=ini//10
        num+=wei*(pow(2,i))
    return num


for i in range(a):
    b=int(input())
    weight=100000000
    four=b%weight
    three=(b//weight)%weight
    two=(b//(weight*weight))%weight
    one=b//(weight*weight*weight)
    print(change(one),end='.')
    print(change(two),end='.')
    print(change(three),end='.')
    print(change(four))
