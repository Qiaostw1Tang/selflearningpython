#字典的操作方法get&keys
a={
    "姓名":"名字",
    "年龄":18,
}
r=a.get("姓名")
print(r)

d=a.get("输出None")
print(d)

c=a.get("赋默认值","m默认值")
print(c)

b={
    "姓名":"名字",
    "年龄":18,
    "技能":{
        "技能1":"python",
        "技能2":"C++"
    }
}
print(b.keys())#不返回嵌套第二层的键