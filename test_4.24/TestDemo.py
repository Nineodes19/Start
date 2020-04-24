# str = input("请输入一个字符串：")
# stra = str[::2]
# print(stra)


# import random
#
# s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
#      "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
#      "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# # 方法1：
#
# for i in range(15):
#     print(random.choice(s), end="")
# print("\n")

# import re
# text ='site sea sue sweet see case sse ssee loses'
# tests = re.findall(r'\bs\S*?e\b',text)
# print(tests)

import random

s = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",

     "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",

     "0","1","2","3","4","5","6","7","8","9","@","$","#","&","_","~"]
for i in range(15):
    for j in range(10):
        print(random.choice(s),end="")
    print()
