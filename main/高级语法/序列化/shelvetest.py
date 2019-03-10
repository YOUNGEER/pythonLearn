import shelve
shv=shelve.open(r'test1.db')
shv['a']=1
shv['b']=2
shv['c']=3
shv.close()
