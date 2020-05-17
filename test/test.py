import os
import re
import xlwt
import xlrd
class Songpoems:
    def __init__(self):
        self.ID = ''
        self.name = ''
        self.author = ''
        self.content = ''
        self.thounght = ''
        self.sum = 0

def Init(poemlist):
    file_object = open('C:/Users/Administrator/Desktop/python/poems.txt',"r+")
    for line in file_object:
        sp = Songpoems()
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
        main()
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
            sp = Songpoems()
            sp.ID = input("请输入宋词的名称:>>")
            while True:
                sp.ID = input("请输入宋词的编号:>>")
                p = re.compile('^[0-9]$')
                if p.math(sp.ID):
                    break
                else:
                    print("输入的ID有错误！")
            sp.author = input("请输入宋词的作者:>>")
            sp.content = input("请输入宋词的内容:>>")
            sp.thounght = input("请输入宋词的思想:>>")



if __name__ == "__main__":
    poemlist = []
    Init(poemlist)