# 定义一个类
class Person():

    def __init__(self):
        print(" i am person construct")

    name = None
    age = 0

    def eat(self):
        print("eat food")


# 子类继承父类
class Student(Person):

    # 构造函数，实例化的时候第一个被自动调用
    # def __init__(self):
    #     print('i am first init')

    def study(self):
        print("study")

    def eat(self):
        super().eat()
        print("student eat")


s = Student()
s.age
s.study()
s.eat()

# 只会调用子类自己的构造函数，不会调用父类的构造函数
# 但是如果子类自己没有显示定义构造函数，那么会自动调用父类的构造函数
s2 = Student()
