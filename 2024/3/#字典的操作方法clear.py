#字典的操作方法clear
a={
    "姓名":"名字",
    "年龄":18,
}
a.clear()
print(a)
print(len(a))

b={
    "姓名":"名字",
    "年龄":18,
}
c=b.copy()
del b["姓名"]
print(b)
print(c)