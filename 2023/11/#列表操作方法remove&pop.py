#列表操作方法remove&pop
a=["hello","hi","thanks","hello"]
a.remove("hello")#移除匹配到的第一个“hello”
print(a)
b=["hi","hello","thanks","hello","hi"]
b.pop(3)#移除指定项
print(b)
print(b.pop(3))#输出要移除的字符串