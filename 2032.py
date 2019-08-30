while(True):
    try:
        a,b=map(float, input().strip().split())
        new_a = list(str(a))
        new_b = list(str(b))
        if a!=b:
            print('It isn\'t xiao qiang')
        else:
            print('It\'s xiao qiang')
    except:
        break