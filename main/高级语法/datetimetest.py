import datetime

# 提供日期和时间的运算和表示

dt=datetime.date(2018,3,26)
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)


from datetime import datetime as dddd
# 参数必须传，可以是随意时间
dt2=dddd(2018,1,1)
# 当前时间
print(dt2.today())
print(dt2.now())

# 获取当前时间
print(dddd.now())