import os
from os import path
import shutil
import sys
import time
import argparse

parser = argparse.ArgumentParser() #建立解析命令物件
parser.add_argument('src',help="從這裡複製")
parser.add_argument('dest',help="目標資料夾路徑")
args = parser.parse_args() # 解析命令參數
print('來源路徑:',args.src)
print('目標路徑:',args.dest)
src=args.src
dest=args.dest
if path.isdir(args.src):#判斷是否為資料夾
    src=path.join(args.src,'')#在args.src後面加上\ ex:args.src=test , src=test\
else:
    print('"{}"不是資料夾路徑!'.format(src))
    sys.exit(2)
if path.isdir(args.dest):
    dest = path.join(args.dest,'')
else:
    print('"{}"不是資料夾路徑!'.format(dest))
    sys.exit(2) # 強制結束python執行



for dir_path, dir_names, file_names in os.walk(src): 
    #dir_path   目前所在路徑
    #folder     目前所在資料夾名稱
    #dir_names  目前所在路徑下所擁有的資料夾
    #file_names 目前所在路徑下所擁有的檔案
 
    folder = dir_path.replace(src,'')
    # ex:
    # src      = C:\Users\user\Desktop\ntub\python\fromhere\
    # dir_path = C:\Users\user\Desktop\ntub\python\fromhere\isDir
    dest_path = dest
 
    print('目前路徑:',dir_path)
    if folder == '':
        print('目前在根目錄')
    else:
        print('資料夾路徑:',folder)
        dest_path = path.join(dest,folder)# dest\folder
        print(dest_path)
        if not path.isdir(dest_path) :#判斷是否在目標路徑存在資料夾
            print('新資料夾:',dest_path)
            #否，則新增一個同名資料夾 
            os.makedirs(dest_path)

    for f in file_names:
        src_path = path.join(dir_path, f) #合併成目標路徑#來源資料夾\檔案名稱
        save_path = path.join(dest_path, f)#要儲存的資料夾\檔案名稱
        print(save_path)
        if not path.isfile(save_path):#查看要儲存的資料夾是否有該檔案
           #若沒有。直接進行複製
            shutil.copy2(src_path,save_path)
        else: 
            #若有，判斷最後修改日期
            src_time = int(path.getmtime(src_path))
            dest_time = int(path.getmtime(save_path))
            print(src_time)
            print(dest_time)
            #若是來源檔案時間>要儲存的資料夾檔案時間
            if src_time > dest_time:
                shutil.copy2(src_path, save_path)## 才進行複製