all = []
max = 0
for i in range(int(input())):
    url = input()
    url = url.split(' ')
    if int(url[1]) > max:
        max = int(url[1])
        all=[]
        all.append(url[0])
    elif int(url[1]) == max:
        all.append(url[0])


for j in all:
    print(j)

