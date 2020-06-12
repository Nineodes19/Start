# class Person:
#     def __init__(self,n,y,w,h):
#         self.name = n
#         self.year = y
#         self.__weight = w
#         self.__height = h
#     def old(self,y):
#         return y - self.year
#
# pa = Person("Lily",2005,50,1.5)
# print("姓名为：",pa.name,"体重为",pa._Person__weight,"千克")
# pa._Person_weight = 48
# print("现在的体重为",pa._Person_weight,"千克")
# myyear = 2015
# myage = pa.old(myyear)
# if myage >0:
#     print("到"+str(myyear) + "年" + str(myage) + "岁")
# elif myage < 0:
#     print(str(myyear) + "年还没出生呢，出生于" + str(pa.year) + "年")
# else:
#     print(str(myyear) + "年刚出生")
