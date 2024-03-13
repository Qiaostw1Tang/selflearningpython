#集合添加元素＆合并集合
a={1,2,3}
a.add(1)
print(a)
#
b={1,2,3}
b.add(6)
print(b)

c={1,2,3}
c.add("一二三")
print(c)

d={1,2,3}
d.add((1,2,3))
print(d)


e={"w","r","I"}
a.update(e)
print(a) #集合的排列是随机排列，谁把谁并进去谁就改变