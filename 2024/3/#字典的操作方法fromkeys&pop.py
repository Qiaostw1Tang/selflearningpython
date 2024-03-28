#字典的操作方法fromkeys&pop
d={}
d1=d.fromkeys(("名字","年龄"))
print(d1)

a={}
a1=a.fromkeys(("名字","年龄"),6)
print(a1)

b={}
b1=b.fromkeys(("名字","年龄"),(1,2))
print(b1)


c={"名字":"姓名",
   "年龄":18
   }
e=c.pop('名字')
print(e)
print(c)