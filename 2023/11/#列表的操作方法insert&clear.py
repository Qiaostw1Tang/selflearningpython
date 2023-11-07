#列表的操作方法insert&clear
a=[10,20,30,40]
a.insert(2,[1,2,3])#[10, 20, [1, 2, 3], 30, 40]
print(a)
b=[10,20,30,40]
b.insert(2,99)
print(b)
a.clear()#[]
print(a)