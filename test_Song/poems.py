
import re # 导入正则表达式模块
import os # 导入操作系统模块
import sys

filename = "poem.txt" # 宋词保存文件
def menu():
 # 输出菜单
 print('''
 ---------------宋词信息管理系统-----------
 ==================功能菜单================
 |------------【1】添加宋词信息-----------|
 |------------【2】查询宋词信息-----------|
 |------------【3】删除宋词信息-----------|
 |------------【4】修改宋词信息-----------|
 |------------【5】按照编号排序-----------|
 |------------【6】统计学生总人数---------|
 |------------【7】显示所有宋词信息-------|
 |------------【0】退出管理系统-----------|
 ======================================= 
        说明:通过数字选择菜单(0-7)
 =======================================
 ''')


def main():
    ctrl = True # 标记是否退出系统
    while (ctrl):
        menu() # 显示菜单
        option = input(">请选择：") # 选择菜单项
        option_str = re.sub("\D", "", option) # 提取数字
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0: # 退出系统
                print('您已退出宋词信息管理系统！')
                ctrl = False
            elif option_int == 1: # 录入宋词信息
                insert()
                sys.stdin.readline()
            elif option_int == 2: # 查找宋词信息
                search()
                sys.stdin.readline()
            elif option_int == 3: # 删除宋词信息
                delete()
                sys.stdin.readline()
            elif option_int == 4: # 修改宋词信息
                modify()
                sys.stdin.readline()
            elif option_int == 5: # 按照宋词ID进行排序
                sort()
                sys.stdin.readline()
            elif option_int == 6: # 统计已录入的宋词总数
                total()
                sys.stdin.readline()
            elif option_int == 7: # 显示所有宋词信息
                show()
                sys.stdin.readline()


'''录入宋词信息'''


def insert():
    poemList = [] # 保存宋词信息的列表
    temp = True # 是否继续添加
    while temp:
        Id = input("\033[1;34;47m>请输入宋词编号ID（如1001）：\033[0m")
        if not Id:
            break
        try:
            Name = str(input("\033[1;34;47m>请输入录入宋词的名称\033[0m"))
            Author = str(input("\033[1;34;47m>请输入录入宋词的作者\033[0m"))
            Content = str(input("\033[1;34;47m>请输入录入宋词的内容\033[0m"))
            Idea = str(input("\033[1;34;47m>请输入录入宋词的思想\033[0m"))
        except:
            print("\033[1;34;47m输入无效，请重新输入信息\033[0m")
            continue
  # 将输入的学生信息保存到字典
        poems = {"id": Id, "name": Name, "author": Author, "content": Content, "idea":Idea }
        poemList.append(poems) # 将学生字典添加到列表中
        inputList = input("\033[1;34;47m>是否继续添加？（y/n）:\033[0m")
        if inputList == 'y': # 继续添加
            temp = True
        else:
            temp = False
    save(poemList) # 将学生信息保存到文件
    print("\033[1;34;47m学生信息录入完毕!!!\033[0m")


'''将宋词信息保存到文件'''


def save(poems):
    try:
        poem_txt = open(filename, 'a') # 以追加模式打开
    except Exception as e:
        poem_txt = open(filename, 'w') # 文件不存在，创建文件并打开
    for info in poems:
        poem_txt.write(str(info) + "\n") # 执行存储，添加换行符
    poem_txt.close() # 关闭文件


'''查询宋词信息'''


def search():
    mark = True
    poem_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            choice = input("\033[1;34;47m按ID查询输入1："
                         "按名称查询输入2："
                         "按作者查询输入3\033[0m")
            if choice == "1":
                id = input("\033[1;34;47m>请输入宋词编号：\033[0m")
            elif choice == "2":
                name = input("\033[1;34;47m>请输入宋词名称：\033[0m")
            elif choice == "3":
                author = input("\033[1;34;47m>请输入作者名：\033[0m")
            else:
                print("\033[1;34;47m您输入有误，请重新输入!\033[0m")
            #search()
            with open(filename, "r") as file:
                poem = file.readlines()
                for list in poem:
                    d = dict(eval(list))
                    if id !="":
                        if d['id'] == id:
                            poem_query.append(d)
                    elif name!="":
                        if d['name'] == name:
                            poem_query.append(d)
                    elif author != "":
                        if d['author']:
                            poem_query.append(d)
                    show_poems(poem_query)
                    poem_query.clear()
                inputMark = input("\033[1;34;47m>是否继续查询?(y/n):\033[0m")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("\033[1;34;47m暂未保存数据信息...\033[0m")
            return


'''将保存在列表中的宋词信息显示出来'''


def show_poems(poemList):
    if not poemList:
        #print("无效的数据")
        return
    format_title = "\033[1;34;47m---{:^6}\033[0m"
    #print(format_title.format("ID", "宋词名", "词人", "内容", "思想"))
    format_data = "\t{:^6}"
    for info in poemList:
        print(format_title.format("ID"))
        print(format_data.format(info.get("id")))
        print(format_title.format("宋词名"))
        print(format_data.format(info.get("name")))
        print(format_title.format("词人"))
        print(format_data.format(info.get("author")))
        print(format_title.format("内容"))
        print(format_data.format(info.get("content")))
        print(format_title.format("思想"))
        print(format_data.format(info.get("idea")))



'''删除宋词信息'''


def delete():
    mark = True # 标记是否循环
    while mark:
        poemId = input("\033[1;34;47m>请输入要删除的学生ID：\033[0m")
        if poemId !="": # 判断要删除的学生ID是否存在
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    poem_old = rfile.readlines()
            else:
                poem_old = []
                ifdel = False # 标记是否删除
            if poem_old: # 如果存在学生信息
                with open(filename, 'w+') as wfile:
                    d = {} # 定义空字典
                    for list in poem_old:
                        d = dict(eval(list)) # 字符串转字典
                        if d['id'] != poemId:
                            wfile.write(str(d) + "\n") # 将一条信息写入文件
                        else:
                            ifdel = True # 标记已经删除
                    if ifdel:
                        print("\033[1;34;47mID为%s的学生信息已经被删除...\033[0m" % poemId)
                    else:
                        print("\033[1;34;47m没有找到ID为%s的学生信息...\033[0m" % poemId)
            else:
                 print("\033[1;34;47m不存在学生信息")
                 break
            show() # 显示全部学生信息
            inputMark = input("\033[1;34;47m是否继续删除？(y/n):\033[0m")
            if inputMark == "y":
                mark = True # 继续删除
            else:
                mark = False # 退出删除学生信息操作




'''修改宋词信息'''


def modify():
    show() # 显示全部学生信息
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            poem_Id = rfile.readlines()
    else:
        return
    poemid = input("\033[1;34;47m>请输入要修改的学生ID：\033[0m")
    with open(filename, 'w') as wfile:
        for student in poem_Id:
            d = dict(eval(student))
            if d['id'] == poemid:
                print("\033[1;34;47m找到了该宋词，可修改信息\033[0m")
                while True: # 输入要修改的信息
                    try:
                        d["name"] = input("\033[1;34;47m>请输入宋词名称：\033[0m")
                        d["author"] = input("\033[1;34;47m>请输入宋词的作者：\033[0m")
                        d["python"] =input("\033[1;34;47m>请输入宋词的内容：\033[0m")
                        d['c'] = input("\033[1;34;47m>请输入宋词的思想：\033[0m")
                    except:
                        print("\033[1;34;47m您输入有误，请重新输入！\033[0m")
                    else:
                        break
                poems = str(d) # 将字典转为字符串
                wfile.write(poems + "\n") # 将修改信息写入到文件
                print("\033[1;34;47m修改成功\033[0m")
            else:
                wfile.write(poems) # 将未修改的信息写入文件
        mark = input("\033[1;34;47m是否继续修改其他学生信息？(y/n):\033[0m")
        if mark == "y":
            modify()


'''排序'''


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            poem_old = file.readlines()
            poem_new = []
            for list in poem_old:
                d = dict(eval(list))
                poem_new.append(d)
    else:
        return
    ascORdesc = input("\033[1;34;47m>请选择（0升序；1降序）\033[0m")
    if ascORdesc == "0":
        ascORdescBool = False # 标记变量，为False时表示升序，为True时表示降序
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("\033[1;34;47m>您输入的信息有误，请重新输入!\033[0m")
    poem_new.sort(key=lambda x: x["id"], reverse=ascORdescBool)

    show_poems(poem_new) # 显示排序结果


'''统计宋词总数'''


def total():
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            poem_old = rfile.readlines()
            if poem_old:
                print("\033[1;34;47m一共有%d首宋词!\033[0m" % len(poem_old))
            else:
                print("\033[1;34;47m还没有录入宋词！\033[0m")
    else:
        print("\033[1;34;47m暂未保存数据信息\033[0m")


#显示所有宋词信息
def show():
    poem_new = []
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            poem_old = rfile.readlines()
            for list in poem_old:
                poem_new.append(eval(list))
            if poem_new:
                show_poems(poem_new)
            else:
                print("\033[1;34;47m暂未保存数据信息")


if __name__ == '__main__':
    main()