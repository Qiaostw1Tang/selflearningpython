#python的条件语句if
if 3>2:
    print("你好")#必须有缩进，否则报错
if 3>6: #条件必须为真值，否则不执行
    print("你好2")
if True:
    print("你好3")
if False:
    print("你好4")

if 0>1:
    print("你好5")
elif 4>1: #不能缩进，否则报错
    print("你好6")
else:
    print("以上条件均不满足")