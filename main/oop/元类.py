# 元类写法是固定的，它必须继承自type
# 一般以MetaClass结尾

class YuanleiMetaClass(type):

    def __new__(cls, name, bases, attrs):
        print("hahha，元类")
        attrs['id']='0000'
        return type.__new__(cls, name, bases, attrs)


# 元类定义完就可以使用，注意写法
class Teacher(object, metaclass=YuanleiMetaClass):
    pass


t = Teacher()
t.id
t.__dict__
