#列表操作方法index&reverse
a=["hello","world","hello","hello","hi"]
r=a.index("hello")
print(r)#输出第一个找到的该字符串位置

r1=a.index("hello",1,3)#指定查找范围
print(r1)
a.reverse()#将列表逆向排序
print(a)