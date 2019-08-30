def f(n, x):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V']
    b = []
    while True:
        s = n // x
        y = n % x
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    for i in b:
        print(a[i], end='')
    print()


while (True):
    try:
        a = int(input())
        for i in range(a):
            N, R = map(int, input().strip().split())
            if N > 0:
                f(N, R)
            elif N == 0:
                print('0')
            else:
                print('-', end='')
                f(-N, R)
    except:
        break