class A():
    def __init__(self):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")

    def __str__(self):
        return "str"

    def __getattr__(self, item):
        print("getattr")
     
    def __setattr__(self, key, value):
        # 调用父类避免死循环
        super().__setattr__(key,value)

a = A()
a()
print(a)
a.name
