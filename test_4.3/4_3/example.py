# #example3_15.py
# # -*- coding: cp936 -*-
#
# strs = ['Mike','Tom','Null','Apple','Betty','Null','Amy',
#         'Dick']
#
# for astr in strs:
#     if astr == 'Null':
#         continue
#
#     for s in astr:
#         if s == 'i':
#             continue
#         print(s,end='')
#
#     print()
#
# print('End')
#
#
# print("所有三位数的素数如下：",end="")
# for i in range():
#    j=2
#    flag=1
#    while j<i:
#       if i % j == 0:
#           flag = 0
#           break
#       j+=1
#    if flag == 1:
#        print(i,end=" ")
#
#
# """程序提示用户输入一个自然数，如果该数不为-1，
# 则根据例3-9的方法计算并输出该自然数除自身外的最大约数；
# 然后提示用户再输入一个自然数，利用循环重新计算并输出
# 该自然数除自身外的最大约数；直到输入为-1时终止该程序。
# """
# print()
# num = int(input('请输入一个自然数：'))
# while num != -1:
#     count = num // 2
#     while count > 0:
#         if num % count == 0:
#             break
#         count = count -1
#
#     print(count,'is the factor of',num)
#     num = int(input('请再输入一个自然数：'))
#
# print('程序结束')


#随机输入一个字符串（五个以上字符）并为其每个字符的ASCII码形成列表并输出
# text = input('请输入一个字符串：')
# arr = []
# n = 0
# for t in text:
#     n += 1
#     arr.append(ord(t))
#
# if n >= 5:
#     print('字符串的ASCCI为：',arr)
# else:
#     print('请输入5个以上字符')


#统计输入的字符串（6 个以上单词）中单词的个数，单词之间用空格分隔。
# string = input('请输入一个字符串：')
# s = []
# flag = 0
# num = 0;
# for s1 in string:
#     if s1 == ' ':
#         flag+=1
#         num += 1
# flag+=1
#
# if num >= 6:
#     print('单词个数为：',flag)
# else:
#     print('请输入6个以上字符')


#：输入一行字符（20 个以上字符），分别统计出其中英文字母、
# 空格、数字和其它字符的个数。

# string1 = input('请输入一个字符串：')
# letter = 0
# blank = 0
# digit = 0
# ch = 0
# for str1 in string1:
#     if str1.isalpha():
#         letter+=1
#     elif str1.isalnum():
#         digit+=1
#     elif str1.isspace():
#         blank+=1
#     else:
#         ch +=1
# print('英文字母：',letter,'个，空格：',blank,'个，数字：',
#       digit,'个，其他字符：',ch,'个')


#任务四：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字
# 的三位数？各是多少？

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k) and (i != j) and (j != k):
                print(i*100+j*10+k,end=" ")
    print()