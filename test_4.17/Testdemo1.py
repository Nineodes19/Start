# a = int(input("请输入一个数字:\n"))
# x = str(a)
# flag = True
#
# for i in range(len(x) >> 1):
#     if x[i] != x[-i - 1]:
#         flag = False
#         break
# if flag:
#     print("%d 是一个回文数!" % a)
# else:
#     print("%d 不是一个回文数!" % a)


# if __name__ == '__main__':
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     print( '原始列表:')
#     for i in range(len(a)):
#         print (a[i],end=" ")
#     number = int(input("\n插入一个数字:\n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     print('排序后列表:')
#     for i in range(11):
#         print(a[i],end=" ")


# for x in range(1,34):
#     for y in range(1,51):
#         for z in range(100):
#             if 3*x+2*y==100-z/2:
#                 if x+y+z==100:
#                     print("大马有",x,"小马有",y,"马驹有",z)


from math import sqrt


def main():
    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        if num % x == 0:
        print('%d不是素数' % num)


if __name__ == '__main__':
    main()
