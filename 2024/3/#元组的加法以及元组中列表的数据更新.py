#元组的加法以及元组中列表的数据更新
t1=("hello","world","python")
t2=([1,2],[3,4],[5,6])
t3=t1+t2
print(t3)
t3[3][0]="哈哈哈哈"
print(t3)