#python的for循环2
d={"名字":"姓名",
   "年龄":18}
for a in d:
    print(a)

print(d.items())
for i in d.items():
    print(i)
    
#range函数步长 range(0,4)->区间0123；range（0,6,2)->2为步长
for j in range(0,6,2):
    print(j)