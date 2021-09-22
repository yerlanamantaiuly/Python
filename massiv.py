import os
import shutil
print("Все папки и файлы:", os.listdir('D:\\1'))

folders = os.listdir('D:\\1')
print(folders[-1])

for x in folders:
    if os.path.isdir(os.path.join('D:\\1', x)):
        a = os.path.join('D:\\1', x)
        files = os.listdir(a)

        print(a)
        #print(files[-1])

        if not files:
            print("pustaya papka" + "  " + a )
        else:
            b = os.path.join(a, files[-1])
            c = 'D:\\2\\' + files[-1]
            shutil.copy(b, c)