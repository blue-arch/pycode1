#任务：将文件（record.txt 下面我会用33.txt代替）中的数据进行分割并按照以下规律保存起来：
#小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼：”）
#小客服的对话单独保存为girl_*.txt的文件（去掉“小客服：”）
#文件中总共有三段对话，分别保存为boy_1.txt，girl_1.txt，boy_2.txt，
#girl_2.txt，boy_3.txt，girl_3.txt共6个文件（提示：文件中的不同对话见已经使用“=========”分割）


'''def save_file(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open('%s' % file_name_boy, 'w')
    girl_file = open('%s' % file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name)
    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split('：', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            count += 1
            boy = []
            girl = []

    save_file(boy, girl, count)
    f.close()


split_file('33.txt')'''

'''try:
    f = open('adad.txt', 'w')
    print(f.write('我存在了'))
    sum = 1 + '1'
    f.close()


except OSError:
    print('文件出错了')
except TypeError as reason:
    print('错误为：' + str(reason))
finally:'''

'''import easygui
import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏')    #msgbox其实还可以设置第二个参数，第二个参数代表标题栏上面的文字，就如下面那个msgbox里面的 '结果'
    msg='请问你希望在鱼C工作室学习到什么知识呢？'
    title='小游戏互动'
    choices=['谈恋爱','编程','OOXX','琴棋书画']
    choice=g.choicebox(msg,title,choices)     #还没看文档，不过这个choicebox这个函数应该是可以接受好几个参数的，包括顶栏的标题，选项内容，已经主语句
    g.msgbox('你的选择是:' + str(choice),'结果')
    msg ='你希望重新开始小游戏吗？'
    title='请选择'
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
'''

'''import easygui as g
import sys
try:
        print('I Love FishC.com!')
        int('FISHC') # 这里会产生异常
except:
        g.exceptionbox()'''


'''class BowlModel:
    make_in = 'China'  # 类变量，不需要实例化就调用

    def __init__(self, colour='red', material='lron'):  # __init__方法一般用来对实例的属性进行初始化
        # 下面两个是实例变量
        self.colour = colour
        self.material = material
        print('颜色：', self.colour, '材料：', self.material)

    # 定义make方法
    def make(self, name):
        print(name, '制作了一只', self.colour, self.material, '碗。')

a = BowlModel()
print (BowlModel.make_in)
print (a.make_in)
a.colour = 'green'
print (vars(a))
print (a.material)
a.factory = '陶瓷厂'
print (vars(a))
a.make('老王')


def company(self, company_name):
    print(company_name, '在制作一只', self.colour, self.material, '碗。')


a.cy = company
a.cy(a,'大大陶瓷厂')'''

'''class Person:
    __name = 'lanqiuwang'
    def getName(self):
        return self.__name

p = Person()
print(p.getName())
print(p._Person__name)'''

'''import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x-=1
        print('我的位置是：',self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self)
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是吃^_^')
            self.hungry = False
        else:
            print('太撑了，吃不下了！')

fish = Fish()
fish.move()
shark = Shark()
shark.move()
shark.eat()'''
#组合















































