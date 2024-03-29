#字典的操作方法popitem&setdefault
c={"名字":"姓名",
   "年龄":18
   }
r= c.popitem()
print(r)
print(c)

a={"名字":"姓名",
   "年龄":18
   }
a.setdefault("技能","能力")
print(a)