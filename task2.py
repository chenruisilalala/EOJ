import os, sys


class Task:
    def showDirTree(self, path):
        ########## BEGIN ##########
        if type(path) == str:
            path = path.split()
            print('+--' + path[0].split('/')[-1])
        dir = os.listdir('/'.join(path))
        dir.sort()
        wenjianjia = []
        for i in dir:
            path.append(i)
            if os.path.isfile('/'.join(path)) != True:
                wenjianjia.append(i)
                print(' ' * 2 * (len(path)) + '+--' + i)
                Task.showDirTree(self, path)
            else:
                if 'jpg' in i[-3:]:
                    print(' ' * 2 * (len(path) - 1) + '--' + i)
                elif 'png' in i[-3:]:
                    print(' ' * 2 * (len(path) - 1) + '--' + i)
                elif 'bmp' in i[-3:]:
                    print(' ' * 2 * (len(path) - 1) + '--' + i)
            path.remove(i)

        # for j in wenjianjia:

        # for k in wenjianjia:
        #    dir.remove(k)
        # for l in dir:
        #   print(' ' * 2 * (len(path)+1 )+ '--' + l)
########## END ##########


########## END ##########