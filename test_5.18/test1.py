# import xlwt
#
#
# f = open('C:/Users/Administrator/Desktop/python/Py7-1.txt','w')
# while True:
#     str = raw_input("input:>>")
#     if str == 'exit':
#         break
#     f.write(str + "\n")
# str1 = '万里长征人未还。'
#
# f.close()
#
#
import xlwt
import re
f = open('C:/Users/Administrator/Desktop/python/Py7-1.txt','w')
while True:
    str = input("input:>>")
    if str == 'exit':
        break
    f.writelines(str + "\n")
f.close()

old_file = 'C:/Users/Administrator/Desktop/python/Py7-1.txt'
fopen = open(old_file,'r')

w_str = ""
for line in fopen:
    if re.search('秦时明月汉时关。',line):
        line = re.sub('秦时明月汉时关。','万里长征人未还。',line)
        w_str+=line
    else:
        w_str+=line
wopen = open(old_file,'w')
wopen.write(w_str)
fopen.close()
wopen.close()
