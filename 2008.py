a = []
for i in range(int(input())):
    a.append(int(input()))
for j in range(int(input())):
    flag = int(input())
    if (flag in a):
        print('yes!')
    else:
        print('no!')
