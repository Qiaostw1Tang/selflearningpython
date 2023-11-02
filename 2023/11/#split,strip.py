#split,strip
s1="111ab222ab333ab444"
print(s1.split('a'))#以a作为分割点分割，以列表输出，形式：['111', 'b222', 'b333', 'b444']
print(s1.split('a',2))#只分割两次，后续不分割保留
s2='        iugiuwg3     78y83     '
print(s2.strip())#去除首尾空格
s3="66666guygugx66666sug776666"
print(s3.strip('6'))#去除首尾6
print(s2.replace(' ',''))#第一个'内打空格，第二个不打，指把空格换成空字符
