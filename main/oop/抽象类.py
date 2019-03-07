import abc


# 抽象类必须声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):

    # 抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类的抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass


class Man(Human):
    def smoking(self):
       print("smoking")

    def drink(cls):
        print("drink")

    def play():
        print("play")