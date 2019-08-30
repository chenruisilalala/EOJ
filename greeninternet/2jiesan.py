def countOfShips(ferry):
    '''********** BEGIN **********'''

    result = 0
    for i in range(len(ferry)):
        for j in range(len(ferry[0])):
            if ferry[i][j] == '+':
                result += 1
                if j != len(ferry[0])-1:
                    if ferry[i][j + 1] == '+':
                        add = 1
                        while ferry[i][j + add] != 'o' and j+add<=len(ferry[0])-2:
                            ferry[i][j + add] = 'o'
                            add += 1
                        ferry[i][j + add]='o'
                if i+1 != len(ferry):
                    if ferry[i + 1][j] == '+':
                        add2 = 1
                        print(i,j)
                        while ferry[i + add2][j] != 'o' and i+add2<=len(ferry)-2:
                            ferry[i + add2][j] = 'o'
                            add2+=1
                        ferry[i + add2][j] = 'o'

    '''********** END ************'''
    return result

a=[['+','o' ,'o' ,'+'],
['o', 'o', 'o', '+'],
['o', 'o', 'o', '+']]
b=countOfShips(a)
print(b)


