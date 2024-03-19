#字典的增删改查的操作

d={"名字":"name","年龄":18}
d["技能"]="skills"
print(d)

b={"名字":"name","年龄":18}
del b["年龄"]
print(b)

c={"名字":"name","年龄":18}
c["名字"]='大名'
print(c)

print(c["名字"])