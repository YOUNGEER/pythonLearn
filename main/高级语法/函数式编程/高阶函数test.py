from functools import reduce

def myAdd(x,y):
    return x+y
res=reduce(myAdd,[1,1,23,56])
print(res)