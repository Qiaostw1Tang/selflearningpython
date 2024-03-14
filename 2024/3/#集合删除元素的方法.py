#集合删除元素的方法
a={"abc","def","ghi"}
a.remove("abc")
print(a) #如没有，则会报错

b={"abc","def","ghi"}
b.pop()
print(b) #随机

c={"abc","def","ghi"}
c.discard("abc")
print(c) #如没有，则不会报错，显示原字符串