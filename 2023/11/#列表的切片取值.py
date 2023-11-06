#列表的切片取值
list1=[10,20,30,40,50,60,70]
print(list1[0:3])#取左不取右，到30为止
print(list1[-3:-1])#[50, 60]
print(list1[-3:])#[50, 60, 70]
print(list1[:])#全部
print(list1[1:6:2])#[20, 40, 60]
print(list1[-6:-1])#[20, 30, 40, 50, 60]
print(list1[-6:-1:2])#[20, 40, 60]
print(list1[::-1])#反向，[70, 60, 50, 40, 30, 20, 10]
print(list1[-2::-3])#[60, 30]
print(list1[3:6])#[40, 50, 60]
print(list1[-2::-1])#[60, 50, 40, 30, 20, 10]
print(list1[-2::-2])#[60, 40, 20]
print(list1[-1::-1])#[70, 60, 50, 40, 30, 20, 10]
print(list1[-3:-6:-1])#[50, 40, 30]