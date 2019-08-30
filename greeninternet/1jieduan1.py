def getSum( num1, num2):
    ########## BEGIN ##########
    startn = 0
    for a in range(num1, num2 + 1):
        b = str(a)
        for i in b:
            startn += int(i)
    print(startn)

getSum( 15, 19)