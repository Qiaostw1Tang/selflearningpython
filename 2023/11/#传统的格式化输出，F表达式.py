#传统的格式化输出，F表达式
s1="我%s你"%(100)
print(s1)
s2="我%s你"%([1,2])
print(s2)
s3='wo%ddjijij'%(100.99)#%d只能写数值，非数值会报错，小数点后忽略不四舍五入，输出整数
print(s3)
s4="我%f你"%(100.123456789)#可以输出小数点后6位数，会四舍五入，其它同%d，浮点型
print(s4)
name='ad'
age=18
s5='我的名字叫{}，我的年龄是{}'.format(name,age)
s6=f'我的名字叫{name}，我的年龄是{age}'
print(s5)
print(s6)