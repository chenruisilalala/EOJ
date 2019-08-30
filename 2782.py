inp = ['E', 'C', "N", 'U', 'Impossible', 'ACM']
ou = ['Excellent', 'Cheer', 'Nice', 'Ultimate', "I'm possible", 'Accept More']
for i in range(int(input())):
    a = input()
    for num in range(6):
        if (a == inp[num]):
            print(ou[num])
            break

