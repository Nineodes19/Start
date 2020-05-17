
# import xlrd
#
# # 造的模拟数据
# re_list= [{'apple':"11.5","orage":"嗯10:00字","xigua":"8.0"},{'apple1':"111.5","orage":"100.9","xigua1":"80.0"}]
# content=[item.pop("orage") for item in re_list if "orage" in item.keys() ]
# # 循环变量造出的数据
# for item in content:
# # 设置字体格式
#     Font0=xlwt.Font()
#     Font0.name="Times New Roman"
#     Font0.colour_index = 2
#     Font0.bold = True # 加粗
#     style0=xlwt.XFStyle()
#     style0.font=Font0
#     #实例化一个execl对象xls=工作薄
#     xls = xlwt.Workbook()
#     # 实例化一个工作表，名叫Sheet1
#     sht1 = xls.add_sheet('ex06.xlsx')
#     # 第一个参数是行，第二个参数是列，第三个参数是值,第四个参数是格式
#     sht1.write(0, 0, '学号',style0)
#     sht1.write(0, 1, '性别',style0)
#     sht1.write(0, 2, '语文',style0)
#     sht1.write(0, 3, '数学',style0)
#     sht1.write(0, 4, '英语', style0)
#     sht1.write(0, 5, '政治', style0)
#     # 4、模拟插入数据
#     sht1.write(1, 0, 'S09')
#     sht1.write(1, 1, '女')
#     sht1.write(1, 2, '89.2')
#     sht1.write(1, 3, '88.4')
#     sht1.write(1, 4, '86')
#     sht1.write(1, 5, '87.9')
# #
#     sht1.write(2, 0, 'S10')
#     sht1.write(2, 1, '女')
#     sht1.write(2, 2, '90.5')
#     sht1.write(2, 3, '86.3')
#     sht1.write(2, 4, '87')
#     sht1.write(2, 5, '87.9')
# #
#     sht1.write(3, 0, 'S11')
#     sht1.write(3, 1, '男')
#     sht1.write(3, 2, '88.7')
#     sht1.write(3, 3, '89.4')
#     sht1.write(3, 4, '89')
#     sht1.write(3, 5, '89.0')
#     xls.save('./mydata.xls')
#

import xlwt
f = open('C:/Users/Administrator/Desktop/python/Py7-1.txt','w')
while True:
    str = raw_input("input:>>")
    if str == 'exit':
        break
    f.write(str + "\n")
f.close()