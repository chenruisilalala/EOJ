while(True):
    try:
        b = []
        a=input()
        while(True):
            c=input()
            if(c==""):
                break
            b.extend((map(int, c.strip().split())))
        if(a=='A'):
            b.sort(reverse=False)
        if(a == 'D'):
            b.sort(reverse=True)
        news = []
        for id in b:
            if id not in news:
                news.append(id)
        for i in range(len(news)-1):
            print(news[i],end=' ')
        print(news[-1],end='')
    except:
        break
