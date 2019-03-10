# 1.模块（python文件）
- 一个模块就是一个包含python代码的文件，后缀名是.py就可以，模块就是个python文件
- 为什么需要用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以如何代码可以直接书写    
    - 不顾根据模块的规范，最好在模块中编写一下代码
        - 函数
        - 类
        - 测试代码
- 如何使用模块
    - 模块直接导入
    - 语法
        - import module_name as name2
        - import importlib
        - from module_name import class,class2 / *
    - if __name__=='__main__' 的是哟
        - 可以有效避免模块代码被导入的时候出现问题
        - 建议每个模块都添加该代码
 
# 2 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的时候，系统会在哪些地方寻找次模块
- 系统默认的模块搜索路径
    - import sys
    - sys.path 属性可以获取路径列表
- 添加搜索路径
    - sys.path.append(dir)
- 模块的加载顺序
    1.上搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path路径
    
# 3 包（多个模块）         
- 包是一个组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构
- __init__.py 包默认创建的文件夹】

## 包的导入操作
- import package_name
    - 直接导入一个包，可以使用__init__.py中的内容
    - 使用方式是：
        - package_name.func_name
        - package_name.class_name.func_name 
    - 此种方式的访问内容是
 - import package_name as p
    - 具体用法跟作用方式，跟上述简单导入一直
 - import package_name.module as p
 - from ... import 导入
    - from package import module ，module2。。
        - 此种导入方法不执行__init__的内容 
    - from package import *
        - 只会执行__init__的内容
 - from package.module_name import *
    - 导入指定的所有内容     
 - 在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块的内容
    - import 完整路径                        
 - __all__的用法
    - 在使用from package import *的时候，* 可以导入的内容
    - `__init__.py`中如果文为空，或者没有`__all__`， 那么只可以把`__init__`中的内容导入 
    - 如果`__init__.py`中设置了`__all__`值， 就按照all指定的模块进行导入
    - __all__=['module1','module2',...]   

# 异常
- 语法
    - try:可能有异常的代码
    - except Error1:出错1
    - except Error2 as e:出现2
    - else:没有出错
    - finally:最后肯定执行  
- 用户手动引发异常
    - 当某些情况，用户希望自己引发一个异常的时候，可以使用
    - raise 关键字来引发异常
    - try：语句1 raise ValueError        
    
# 常用模块,模块需要先导入
## calendar 日历   
## time
## datetime
## timeit
## os
## shutil
## zip
## math
## String

# 函数式编程
## lambda表达式
    - 以lambda开头
    - 紧跟一定的参数（如果有的话）
    - 参数后用冒号和表达式主题隔开
    - 只是一个表达式，没有return
## 高阶函数
- 把函数作为参数使用的函数，叫高阶函数
    - map
    - reduce
    - filter    
    - 排序sorted
    - zip，返回对应tuple
    - enumerate，跟zip类似，但是有索引
- 闭包：内部定义的函数调用了外部定义函数的参数 
- 装饰器
    - 在不改动函数代码的基础上无限制扩展函数功能的一种机制
    - 用@语法使用
- 偏函数
    - 参数固定的函数，相当于一个由特定参数的函数体
    - function.partial的作用是，把一个函数某些函数固定，返回一个新函数
## collections模块
- namedtuple
- deque
- defaultdict
- counter:统计字符串中字符出现的字数           

                           
                              