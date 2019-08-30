import os, sys

class Task:
    def showDirTree(self,path):
        if type(path)==str:
            print('+--'+path)
            path=path.split()
        dir = os.listdir('/'.join(path))
        wenjianjia = []
        for i in dir:
            path.append(i)
            if os.path.isfile('/'.join(path)) != True:
                wenjianjia.append(i)
            path.remove(i)

        for j in wenjianjia:
            print(' ' * 2 * (len(path)) + '+--' + j)
            path.append(j)
            Task.showDirTree(path)
            path.remove(j)
        for k in wenjianjia:
            dir.remove(k)
        for l in dir:
            print(' ' * 2 * (len(path)+1 )+ '--' + l)
########## END ##########