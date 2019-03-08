class ErrorTest(NameError):
    pass


try:
    print("111111111")
    raise ErrorTest
except NameError as e:
    print("name error")
except Exception as e:
    print("exception")
else:
    print("no error")
finally:
    print("肯定会执行")
