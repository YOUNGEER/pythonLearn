# 导入
import p0
stu=p0.Student()
stu.say()


# 借助importlib包可以实现导入以数字开头的模块名称
import importlib
stus=importlib.import_module("p0")

stu2=stus.Student()
stu2.say()


from p0 import Student
stu3=Student()
stu3.say()//48.