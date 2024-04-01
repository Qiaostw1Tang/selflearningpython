#判断某两个对象是否相同is&not
#列表，字典，集合，（可变的数据类型），表面一样，但其实不会被认为是同一个对象
a="一二"
b="python"
print(a is b)
print(a is not b)
c="111"
d="111"
print(c is d)
print(c is not d)
f=[1]
g=[1]
print(f is g)
print(f is not g)
h={"名字":"姓名"}
i={"名字":"姓名"}
print(h is i)
print(h is not i)
j={1,2,3}
k={1,2,3}
print(j is k)
print(j is not k)