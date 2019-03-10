import time
# 时间戳
# UTC事件
# 夏令时
# 时间元组


# 1. timezone:当前时区和UTC事件相差的秒数，没有夏令时
# 2. altzine 当前时区和UTC事件相差的秒数，有夏令时
# 3. daylight:测试当前是否是夏令时状态，0表示否

# 4.time事件戳
print(time.timezone)


# 5. localtime，得到当前时间的时间结构，可以通过点号获取属性内容
t=time.localtime()
# 格式化事件sactime
tt=time.asctime(t)
print(tt)

# 6 ctime：获取字符串化的当前时间

# 7  mktime 使用时间元组获取对应的时间戳
# 格式，time.mktime(时间元组)

# 8 sleep：使程序进入睡眠，n秒后执行

#  strftime：将时间元组转化为自定义的字符串格式