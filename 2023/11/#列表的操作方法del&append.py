#列表的操作方法del&append
a=[1,2,3]
del a #在计算机（内存）中，a定义列表 删除
b=[1,2,3]
del b[1] #删除列表中下标为1的值
print(b)
print(b.append(4))#不存在，输出None
c=[1,2,3,4]
c.append(9)#[1, 2, 3, 4, 9]
print(c)