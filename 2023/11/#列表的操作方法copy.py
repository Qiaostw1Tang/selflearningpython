#列表的操作方法copy
a=["hello","hi","hello","good"]
b=a.copy()#复制列表给b
del a[0]
print(b)#b不受影响
a=["hello","hi","hello","good"]
c=a 
del a[0]
print(c)#c受影响
