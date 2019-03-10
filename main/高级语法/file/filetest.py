# 以写方式打开文件，默认是如果没有文件，则创建
# f=open("__crate1_.txt",'w')
# f.close()


# 读方式对f操作
# 不需要close
# with open(r'crate1.txt','r') as f:
#     pass


with open(r"__crate1_.txt", 'r') as f1:
    # -------readline-----------
    # strline=f1.readline()
    # while strline:
    #     print(strline)
    #     strline=f1.readline()

    # ---------list----------
    # l=list(f)
    # for line in l:
    #     print(line)

    # ---------read---------
    # 按照字符读取，参数1表述读取一个字符
    # f1.seek(4,0)
    # strchar = f1.read(1)
    # print(strchar)

    # seek 移动指针的位置
    # f1.seek(4, 0)
    # strchar = f1.read()
    # print(strchar)

    # tell 显示读写指针的位置
    while f1.read(1):
        print(f1.tell())



with open(r"__crate1_.txt", 'a') as f2:
    f2.writelines("00000000")
    f2.writelines("ffss")

