#find,count
s1="123456789012345678901234567890"
print(s1.find("1",0,26))#从第零到第26个字符间寻找并指出第一次出现字符“1”的位置
print(s1.find("a",0,26))#没有则输出-1
print(s1.count("a"))
print(s1.count("9",6,20))#统计字符出现次数，没有则输出零