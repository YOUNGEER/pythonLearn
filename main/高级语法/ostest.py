# os 操作系统目录相关
# os.path 高级文件操作，目录树的操作，文件赋值，删除，移动
#  绝对路径，相对路径

import os
# 1.获取当前的工作目录
mydir=os.getcwd()
print(mydir)

# 2.改变当前的工作目录
# os.chdir('')

# 文件所在目录的子文件
dirs=os.listdir()
print(dirs)
