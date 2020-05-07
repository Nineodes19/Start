import re



def phone():
    n = ['13915556234','15325645124','15202362459']
    for m in n:
        if re.match(r"13[4,5,6,7,8,9]\d{8}", m) or \
                re.match(r"147\d{8}|178\d{8}", m )or \
                re.match(r"15[0,1,2,7,8,9]\d{8}", m) or \
                re.match(r"18[2,3,4,7,8]\d{8}", m):
            print(m,"该号码属于：中国移动")
        else:
            print("FALSE")

if __name__ == '__main__':
    phone()


#
# vowel = ['a', 'e', 'i','o', 'u','A','E','I','O','U']
#
#
# str = input('请输入字符串：')
#
# sum = 0
#
# for i in str:
#
#     if i in vowel:
#
#         sum+=1
#
# print(sum)