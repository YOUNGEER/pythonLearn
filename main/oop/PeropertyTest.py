class Person():

    # 函数的名称可以随意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name进行操作")


p1 = Person()
# 可以动态设置属性，并且按照set函数
p1.name = "wy"
p1.height = "177"

p1.age = 12
# WYWY
print(p1.name)
print(p1.age)
print(p1.height)
