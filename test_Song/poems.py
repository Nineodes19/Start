import os
import re
import xlwt
import xlrd

class SongPoems:
    def __init__(self):
        self.ID = ''
        self.name = ''
        self.author = ''
        self.content = ''
        self.thounght = ''
        self.sum = 0

#按照编号查找该编号是否已经存在
def searchByID(poemlist,ID):
    for item in poemlist:
        if item.ID == ID:
            return True

#添加一个宋词信息
def Add(poemlist,sp):
    if searchByID(poemlist,sp.ID) == True:
        print("该编号已存在！")
        return False
    poemlist.append(sp)
    print("____________________________________")
    print("|",sp.ID,"|",sp.name,"|",sp.author,"|",sp.content,"|",sp.thounght,"|")
    print("是否保存宋词信息？")
    choose = input("choose Y ？ N ")
    if choose == 'Y' or choose == 'y':
        file = open("C:/Users/Administrator/Desktop/python/poems.txt","w+")
        file.write(sp.ID)
        file.writelines(" ")
        file.write(sp.name)
        file.writelines(" ")
        file.write(sp.author)
        file.writelines(" ")
        file.writelines(sp.content)
        file.writelines(" ")
        file.writelines(sp.thounght)
        sp.sum +=1
        file.close()
        print(u"----------------保存成功！----------------")



def Init(poemlist):
    print("初始化...")
    file_object = open('C:/Users/Administrator/Desktop/python/poems.txt','r+')
    for line in file_object:
        sp = SongPoems()
        line = line.strip("\n")
        s = line.split(" ")
        sp.ID = s[0]
        sp.name = s[1]
        sp.author = s[3]
        sp.content = s[4]
        sp.thounght = s[5]
        poemlist.append(sp)
        file_object.close()
    print("初始化成功！")
def main():

        #菜单栏
        print("____________________________________")
        print(u"|--------欢迎使用宋词管理系统---------|")
        print(u"|----------------菜单----------------|")
        print(u"|----------【1】添加宋词信息---------|")
        print(u"|----------【2】查询宋词信息---------|")
        print(u"|----------【3】修改宋词信息---------|")
        print(u"|----------【4】删除宋词信息---------|")
        print(u"|----------【5】输出所有信息---------|")
        print(u"|----------【6】按照编号排序---------|")
        print(u"|----------【0】退出管理系统---------|")
        print("|___________________________________|")

        choose = input("请输入你的操作选择：>>")

        if choose == "1":
            sp = SongPoems()
            sp.ID = input("请输入宋词的名称:>>")
            while True:
                sp.ID = input("请输入宋词的编号:>>")
                p = re.compile('^[0-9]{3}$')
                if p.match(sp.ID):
                    break
                else:
                    print("输入的ID有错误！")
            sp.author = input("请输入宋词的作者:>>")
            sp.content = input("请输入宋词的内容:>>")
            sp.thounght = input("请输入宋词的思想:>>")
            Add(poemlist,sp)


if __name__ == "__main__":
    poemlist = []
    Init(poemlist)
    main()