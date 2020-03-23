"""
请输入星期几的第一个字母来判断一下是星期几
如果第一个字母一样，则继续判断第二个字母
"""

d = input('请输入字母：')

#Monday Tuesday Wednesday Thursday Friday Saturday Sunday
if d =="M":
    print('星期一')
elif d == "T":
    second = input('请输入第二个字母：')

    if second == "u":
        print('星期二')
    elif second == "h":
        print('星期四')
elif d == "W":
    print('星期三')
elif d == "F":
    print('星期五')
elif d == 'S':
    second = input('请输入第二个字母：')
    if second == "a":
        print('星期六')
    elif second == "u":
        print('星期天')
    else:
        print('第二个字母输入错误！！')
else:
    print('第一个字母输入错误！！')