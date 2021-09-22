##подключаем библиотеки
import os
import shutil
##выводим список Всех папок в ежедневных бэкапах
print("Все папки и файлы:", os.listdir('D:\\source'))
#создаем массив из списка папок
folders = os.listdir('D:\\source')
#создаем цикл в котором проверяем что цель папка а не файл, затем для каждой папки из массива создаем полный путь
# и присваеваем его перемнной a, затем создаем массив из его содержимого среди которых выбираем последнии и копируем его
for x in folders:
    if os.path.isdir(os.path.join('D:\\source', x)):
        a = os.path.join('D:\\source', x)
        files = os.listdir(a)
        print(a)
        #проверяем чтобы массив был не пустой
        if not files:
            print("pustaya papka" + "  " + a )
        else:
            b = os.path.join(a, files[-1])
            c = 'E:\\target\\' + files[-1]
            shutil.copy(b, c)