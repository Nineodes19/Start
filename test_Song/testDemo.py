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
def searchByID(ID):
    for item in poemlist:
        if item.ID == ID:
            return True

#添加一个宋词信息
def Add(poemlist,sp):
    if searchByID(sp.ID) == True:
        print("该编号已存在！")
        return False
    else:
        poemlist.append(sp)
        print("____________________________________")
        print("|编号:",sp.ID,"|名称：",sp.name,"|作者",sp.author,"|内容：",sp.content,"|思想：",sp.thounght,"|")
        print("是否保存宋词信息？")
        choose = input("choose Y ？ N ")
        if choose == 'Y' or choose == 'y':
            file = open("C:/Users/Administrator/Desktop/python/poems.txt","a")
            file.write(sp.ID)
            file.writelines(" ")
            file.write(sp.name)
            file.writelines(" ")
            file.write(sp.author)
            file.writelines(" ")
            file.writelines(sp.content)
            file.writelines(" ")
            file.writelines(sp.thounght)
            file.writelines("\n")
            sp.sum +=1
            poemlist.append(sp)
            file.close()
            print(u"----------------保存成功！----------------")

def Search(poemlist,ID):
    count = 0
    for sp in poemlist:
        if sp.ID == ID:
            print("|编号:",  "|名称：",  "|作者", "|内容：",  "|思想：", "|")
            print (sp.ID, "\t", sp.name, "\t", sp.author, "\t", sp.content, "\t：", sp.thounght, "|")
            break
        count = 0
    if count == len(poemlist):
        print("没有该宋词编号")

def Change(poemlist,ID):
    count = 0
    for item in poemlist:
        if item.ID == ID:
            poemlist.remove(item)
            file = open("C:/Users/Administrator/Desktop/python/poems.txt","w")
            for sp in poemlist:
                file.write(sp.ID)
                file.write(" ")
                file.write(sp.name)
                file.write(" ")
                file.write(sp.author)
                file.write(" ")
                file.write(sp.content)
                file.write(" ")
                file.write(sp.thounght)
                file.write(" ")
        file.close()
        sp = SongPoems()
        while True:
            sp.ID = input("请输入宋词的编号:>>")
            p = re.compile('^[0-9]{3}$')
            if p.match(sp.ID):
                break
            else:
                print("输入的ID有错误！")
        sp.name = input("请输入宋词的名称:>>")

        sp.author = input("请输入宋词的作者:>>")
        sp.content = input("请输入宋词的内容:>>")
        sp.thounght = input("请输入宋词的思想:>>")
        Add(poemlist,sp)

def display(poemlist):

    print("|编号:",  "|名称：",  "|作者", "|内容：",  "|思想：", "|")
    for sp in poemlist:
        print (sp.ID, "\t", sp.name, "\t", sp.author, "\t", sp.content, "\t：", sp.thounght, "|")

def delete(poemlist,ID):
    count = 0
    for item in poemlist:
        if item.ID == ID:
            poemlist.remove(item)
            print("删除成功")
            break
        count+=1
    file = open("C:/Users/Administrator/Desktop/python/poems.txt", "a+")
    for poem in poemlist:
        print("|编号:", "|名称：", "|作者", "|内容：", "|思想：", "|")
        file.write(sp.ID)
        file.write(" ")
        file.write(sp.name)
        file.write(" ")
        file.write(sp.author)
        file.write(" ")
        file.write(sp.content)
        file.write(" ")
        file.write(sp.thounght)
        file.write("\n")
    file.close()

def sort(poemlist):
    Sp = []
    sum = []
    for li in poemlist:
        temp=[]
        temp.append(li.ID)
        temp.append(li.name)
        temp.append(li.author)
        temp.append(li.content)
        temp.append(li.thought)
        Sp.append(temp)
    insertSort(sum,poemlist)
    display(poemlist)
def insertSort(a,poemlist):
    for i in range(len(a) - 1):
        for j in range(i+1,len(a)):
            if a[i] < a[j]:
                temp = poemlist[i]
                poemlist[i] = poemlist[j]
                poemlist[j] = temp
def Init(poemlist):
    print("初始化...")
    file_object = open('C:/Users/Administrator/Desktop/python/poems.txt','a+')
    for line in file_object:
        sp = SongPoems()
        line = line.strip("\n")
        s = line.split(" ")
        sp.ID = s[0]
        sp.name = s[1]
        sp.author = s[2]
        sp.content = s[3]
        sp.thounght = s[4]
        sp.sum = s[5]
        poemlist.append(sp)

    file_object.close()
    print("初始化成功！")

def main():
    while(True):
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
            while True:
                sp.ID = input("请输入宋词的编号:>>")
                p = re.compile('^[0-9]{3}$')
                if p.match(sp.ID):
                    break
                else:
                    print("输入的ID有错误！")

            sp.name = input("请输入宋词的名称:>>")

            sp.author = input("请输入宋词的作者:>>")
            sp.content = input("请输入宋词的内容:>>")
            sp.thounght = input("请输入宋词的思想:>>")
            Add(poemlist,sp)
        elif (choose == "2"):
            ID = input("请输入要查询的ID：")
            Search(poemlist,ID)
        elif (choose == "3"):
            ID = input("请输入要修改的宋词ID：")
            Change(poemlist,ID)
        elif (choose == "4"):
            ID = input("请输入要删除的宋词ID：")
            delete(poemlist)
        elif(choose == "5"):
            display(poemlist)
        elif(choose == "6"):
            sort(poemlist)
        else:
            exit()






if __name__ == "__main__":
    poemlist = []
    Init(poemlist)
    main()