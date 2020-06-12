# s = "hello"
# s1 = s.upper()
# s1
# print(s1)

# _new_()  _init_()
# 当创建一个类对象时，最先被调用的是_new_()方法。
# _new_()方法用于创建对象。_new_()福能股份创建完对象之后，将该对象传递给
# _init_()方法中的self参数，而_init_()非让发是在对象创建完成之后初始化对象状态

#鸟类Bird的定义
class Bird:
    have_feather = True
    way_of_reproduction = 'egg'
    way_of_song = '叽叽喳喳'
    def move(self):
        print('飞飞飞')

