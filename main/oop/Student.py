'''
定义类
'''

# 定义一个空类
class Student:
    pass

# 定义一个对象
mingyue=Student()

# 定义一个类，用来描述学Python的学生
class PythonStudent():
    name=None
    age=19
    course="Python"
    __height=177

    # 需要注意缩进
    # 系统默认有一个slf参数
    def doHomework(self):
        print(" i do homework")
        return None

    def changeFiled(self):
        self.age=20
        self.course="java"
        self.__height=178

    def leiInvoke():
        print("只能通过类名调用该方法")

    # __class__方法可以类型成 类对象
    def classChanage():
        __class__.age=20
        print(__class__.age)
        return None

    # 构造函数类似功能的魔术方法
    def __init__(self):
        self.age=45
        self.name="ww"
        return None

    # 主要拥有name对象的对象都可以传入，利用是鸭子模型，比如class B
    def say(self):
        print(self.name)
        return None
class B():
    name="bbbbbbb"






# 实例化一个对象
yueyue=PythonStudent()
yueyue.doHomework()
# 类实例和普通实例，未重新赋值的属性，指向同一个对象
print(id(PythonStudent.age))
print(id(yueyue.age))

# 类实例和普通实例，重新赋值的属性，指向同一个对象
yueyue.age=18
print(id(PythonStudent.age))
print(id(yueyue.age))

yueyue.changeFiled()
print(yueyue.course)

PythonStudent.say(B)
print(yueyue._PythonStudent__height)

