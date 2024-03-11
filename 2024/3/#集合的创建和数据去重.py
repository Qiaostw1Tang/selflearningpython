#集合的创建和数据去重
a=set("1234")
print(a)
b=set([10,20,30])
print(b)

c=set((1,2,3,4))
print(c)

#字典
d={
    "年龄":18,
    "名字":"汤言策"
}
f=set(d)
print(f)

#变量名={} 元组/字符串/数字,不能写入列表或字典

aa={1,2,3,(1,2,3),"123"}
print(aa)


#列表的去重
a=set([1,2,1,1,1,1,1])
print(a)

bb=set((1,1,1,1))
print(bb)

#字典去重

cc={
    "名字":"汤言策",
    "名字":"汤言策"
}
print(cc)

ff={
    "名字":"汤",
    "名字":"汤言策"
}
print(ff)

zz=set("1211111")
print(zz)

abc={1,2,1,1,1,"12111"}
print(abc)

abcd={1,2,1,1,1}
print(abcd)