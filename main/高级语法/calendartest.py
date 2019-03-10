import calendar

# 1.isleap判断是否是闰年
print(calendar.isleap(2000))

# 2. calendar:获取一年的日历字符串
# 参数
# w=每个日期之间的间隔字符数
# l=每周所占用的行数
# c=每个月之间的间隔字符数
cal1 = calendar.calendar(2019)
print(cal1)
print(type(cal1))

cal2 = calendar.calendar(2019, l=1, c=5)
print(cal2)

# 3.monthrange() 获取某个月周几（0表示周一）开始和月数
# 返回的是一个元组
cal3=calendar.monthrange(2019,3)
print(cal3)

# 用两个值接收
cal4,cal5=calendar.monthrange(2019,3)
print(cal4)
print(cal5)

# 4.monthcalendar 获取月的天数矩阵

# 5. prcal 直接打印日历

# 6. weekday 获取周几