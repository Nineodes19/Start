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
# print("������λ�����������£�",end="")
# for i in range(100,1000):
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
# """������ʾ�û�����һ����Ȼ�������������Ϊ-1��
# �������3-9�ķ������㲢�������Ȼ��������������Լ����
# Ȼ����ʾ�û�������һ����Ȼ��������ѭ�����¼��㲢���
# ����Ȼ��������������Լ����ֱ������Ϊ-1ʱ��ֹ�ó���
# """
# print()
# num = int(input('������һ����Ȼ����'))
# while num != -1:
#     count = num // 2
#     while count > 0:
#         if num % count == 0:
#             break
#         count = count -1
#
#     print(count,'is the factor of',num)
#     num = int(input('��������һ����Ȼ����'))
#
# print('�������')


#�������һ���ַ�������������ַ�����Ϊ��ÿ���ַ���ASCII���γ��б����
# text = input('������һ���ַ�����')
# arr = []
# n = 0
# for t in text:
#     n += 1
#     arr.append(ord(t))
#
# if n >= 5:
#     print('�ַ�����ASCCIΪ��',arr)
# else:
#     print('������5�������ַ�')


#ͳ��������ַ�����6 �����ϵ��ʣ��е��ʵĸ���������֮���ÿո�ָ���
# string = input('������һ���ַ�����')
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
#     print('���ʸ���Ϊ��',flag)
# else:
#     print('������6�������ַ�')


#������һ���ַ���20 �������ַ������ֱ�ͳ�Ƴ�����Ӣ����ĸ��
# �ո����ֺ������ַ��ĸ�����

# string1 = input('������һ���ַ�����')
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
# print('Ӣ����ĸ��',letter,'�����ո�',blank,'�������֣�',
#       digit,'���������ַ���',ch,'��')


#�����ģ����ĸ����֣�1��2��3��4������ɶ��ٸ�������ͬ�����ظ�����
# ����λ�������Ƕ��٣�

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k) and (i != j) and (j != k):
                print(i*100+j*10+k,end=" ")
    print()