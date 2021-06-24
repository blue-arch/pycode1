#第三十课：文件系统：介绍一个高大上的东西
#0.编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：
'''import os
all_files = os.listdir(os.curdir)
dict1 = {}

for line in all_files:
    if os.path.isdir(line):
        dict1.setdefault('文件夹',0)
        dict1['文件夹'] += 1
    else:
        ext = os.path.splitext(line)[1]  # 返回的是元组，获取文件的后缀名=ext
        dict1.setdefault(ext, 0)
        dict1[ext] += 1

for each_line in dict1.keys():
    print('该文件类型下共有类型为%s的文件 %d 个'%(each_line,dict1[each_line]))
'''

#1. 编写一个程序，计算当前文件夹下所有文件的大小，程序实现如图：
'''import os

def file_size():
    all_files = os.listdir(os.curdir)
    dict1 = {}
    for line in all_files:
        if os.path.isfile(line):
            dict1.setdefault(line,os.path.getsize(line))
            print('文件 %s 的大小为 %d 字节！'%(line,dict1[line]))

file_size()'''

#2. 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图：
import os
#想法有问题，
'''a = input('请输入要查找的初始目录:')
b = input('请输入要查找的目标文件：')
all_files = os.listdir(a)
for line in all_files:
    if os.path.isfile(line):


    elif line == b:
        print()'''

'''import os
def search_file(startdir,target):
    os.chdir(startdir)

    for line in os.listdir(os.curdir):
        if line == target:
            print(os.getcwd() + os.sep + line)
        if os.path.isdir(line):
            search_file(line,target)
            os.chdir(os.pardir)
startdir = input('请输入要查找的初始目录:')
target = input('请输入要查找的目标文件：')
search_file(startdir,target)
'''

#3. 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4, rmvb, avi的格式即可），并把创建一个文件（vedioList.txt）存放所有找到的文件的路径，程序实现如图：
'''import os
list1 = []
def classify(startdir):
    os.chdir(startdir)
    allfiles = os.listdir(os.curdir)
    for line in allfiles:
        if os.path.isfile(line):
            ext = os.path.splitext(line)[1]
            if ext in ['.mp4','.rmvb','.avi','.txt','.py']:
                list1.append(os.getcwd() + os.sep + line+os.linesep)
        if os.path.isdir(line):
            classify(line)  # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
    return list1

startdir = input('请输入初始路径：')
list2 = classify(startdir)
f = open("D:\Pycode1//after_work\VedioList.txt", 'w')
f.writelines(list2)
f.close()'''

#4. 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图：
#我写的这个只能查到关键字在哪且程序太混乱
'''import os

def print_keywords(key_word,startdir):
    os.chdir(startdir)
    allfiles = os.listdir(os.curdir)
    for line in allfiles:
        if os.path.isfile(line):
            ext = os.path.splitext(line)[1]
            if ext == '.txt':
                count = 0
                count_position = 0
                f = open(line,encoding='gb18030', errors='ignore')
                for i in f:
                    count += 1
                    if key_word in i:
                        count_position += 1
                        name = os.getcwd() + os.sep + line
                        print('在文件%s中找到了关键字%s'%(name,key_word))
                f.close()
                if count_position != 0:
                    print('=============================================')
                #list1.append(os.getcwd() + os.sep + line + os.linesep)
        if os.path.isdir(line):
            print_keywords(key_word,line)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录

key_word = input('请将该脚本放入待查找的文件夹内，请输入关键字：')
a = input('请问是否要打印关键字在文件夹中的位置（yes/no)：')
if a == 'yes':
    print_keywords(key_word,'D:\Pycode1//after_work')'''

#使用函数分块来实现功能
#有点绕啊
'''import os

def search_in_file(file_name,key):
    f = open(file_name,encoding='gb18030', errors='ignore')
    count = 0
    key_dict = dict() # 字典，用户存放key所在具体行数对应具体位置
    for line in f:
        count += 1
        pos = pos_in_line(line, key) # key在每行对应的位置
        if pos != []:
            key_dict[count] = pos
    f.close()
    return key_dict

#关键字在每行的位置
def pos_in_line(line,key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1) # 用户的角度是从1开始数
        begin = line.find(key,begin+1) # 从下一个位置继续查找
    return pos

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for key in keys:
        print('关键字出现在第%s行，第%s个位置。'%(key,str(key_dict[key])))

#找txt文件
def search_files(key,detail):
    all_files = os.walk(os.getcwd())
    txt_files = []
    for i in all_files:
        for line in i[2]:
            if os.path.splitext(line)[1] == '.txt':
                file = os.path.join(i[0],line)
                #file = i[0] + '\\' + line
                txt_files.append(file)
    for each_txtfile in txt_files:
        key_dict = search_in_file(each_txtfile,key)
        if key_dict:
            print('===============================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txtfile, key))
            if detail in ['y','Y','yes','YES']:
                print_pos(key_dict)

key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)'''

#right answer
#在那里处理掉了空列表？？？？？？？
'''import os


def print_pos(key_dict):  # 负责打印
    keys = key_dict.keys()
    keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))


def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    #print(pos)
    while begin != -1:
        pos.append(begin + 1)  # 用户的角度是从1开始数
        begin = line.find(key, begin + 1)  # 从下一个位置继续查找
    #print(pos)
    return pos


def search_in_file(file_name, key):
    f = open(file_name,encoding='gb18030', errors='ignore')
    count = 0  # 记录行数
    key_dict = dict()  # 字典，用户存放key所在具体行数对应具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)  # key在每行对应的位置
            key_dict[count] = pos

    f.close()
    return key_dict


def search_files(key, detail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes', 'Y', 'y']:
                print_pos(key_dict)


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)
'''

#第三十一课：文件：腌制一缸美味的泡菜
#0. 编写一个程序，这次要求使用pickle将文件（33.txt）里的对话按照以下要求腌制成不同文件（没错，是第29讲的内容小改，考考你自己能写出来吗？这这里建议下载后的33.txt文件最后在自己的本地新建一个同名文件，再把内容拷贝进去，避免一些由于编码造成的报错
'''import pickle

def save_pickle_file(boy,girl,count):
    file_name_boy = boy +str(count) +',txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_pickle_file = open(file_name_boy, 'wb')
    girl_pickle_file = open(file_name_girl, 'wb')

    pickle.dump(boy, boy_pickle_file)
    pickle.dump(girl, girl_pickle_file)

    boy_pickle_file.close()
    girl_pickle_file.close()

def split_file(file_name):
    f = open(file_name)
    boy = []
    girl = []
    count = 1
    for line in f:
        if line[:6] !='======':
            (a,b) = line.split(':',1)
            if a == '小甲鱼':
                boy.append(b)
            if a == '小客服':
                girl.clear(b)

        else:
            save_pickle_file(boy, girl, count)
            count += 1
            boy = []
            girl = []

    save_pickle_file(boy, girl, count)

split_file('record.txt')'''

#第三十三课：异常处理：try-except、try-finally、raise语句
'''try:
    sum = 1 + '1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦T_T\n错误原因是：' + str(reason))
except TypeError as reason:
    print('类型出错啦T_T\n错误原因是：' + str(reason))'''

'''try:
    int('abc')
    sum = 1 + '1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()
except (OSError, TypeError, ValueError) as reason:
    print('出错啦T_T\n错误原因是：' + str(reason))'''

#请恢复以下代码中马赛克挡住的内容，使得程序执行后可以按要求输出。

'''try:
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i,j)
except KeyboardInterrupt:
    print('退出啦！')'''

#0. 还记得我们第一个小游戏吗？只要用户输入非整型数据，程序立刻就会蹦出不和谐的异常信息然后崩溃。请使用刚学的异常处理方法修改以下程序，提高用户体验。

'''import random

secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
try:
    guess = int(temp)
except ValueError:
    print('输入错误！')
    guess = secret
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")'''


#1. input() 函数有可能产生两类异常：EOFError（文件末尾endoffile，当用户按下组合键 Ctrl+d 产生）和 KeyboardInterrupt（取消输入，当用户按下组合键 Ctrl+c 产生），再次修改上边代码，捕获处理 input() 的两类异常，提高用户体验。
'''def int_input():

    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")

    try:
        guess = int(temp)
    except (ValueError, EOFError, KeyboardInterrupt):
        print('输入错误！')
    else:
        return guess

import random

secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')

guess = int_input()
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int_input()
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")'''

#2. 尝试一个新的函数 int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入。
'''def int_input():
    while True:
        try:
            temp = int(input('请输入一个整数：'))
            break
        except ValueError:
            print('出错了，您输入的不是整数！')

int_input()'''

#3. 把文件关闭放在 finally 语句块中执行还是会出现问题，像下边这个代码，当前文件夹中并不存在"My_File.txt"这个文件，那么程序执行起来会发生什么事情呢？你有办法解决这个问题吗？
#way 1
'''try:
    f = open('My_File.txt','x') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    f.close()'''

#way 2
'''try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    if 'f' in locals(): # 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()
'''
#第三十四课：异常处理：丰富的else语句和简洁的with语句
#求素数以及最大约数
'''def showMaxFactor(num):
    count = num//2
    while count > 1:
        if int(num) % int(count) == 0:
            print("%d的最大约数有%d!"%(num,count))
            break
        count -= 1
    else:
        print('%d是素数'%num)


num = int(input('请输入一个整数：'))
showMaxFactor(num)'''

#1.你可以利用异常的原理，修改下面的代码使得更高效率的实现吗？
'''print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name + ' : ' + contacts[name])
        else:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        else:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        if name in contacts:
            del(contacts[name])         # 也可以使用dict.pop()
        else:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')'''

#修改后的代码
'''print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:
            print(name + ' : ' + contacts[name])
        except KeyError:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:
            contacts[name] 
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        try:
            del(contacts[name]) # 也可以使用dict.pop()
        except KeyError:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')'''

#  第三十五课：图形用户界面入门：EasyGui
#  0. 先练练手，把我们的刚开始的那个猜数字小游戏加上界面吧？
#  *********************************************************
#               猜数字小游戏，每轮有三次机会
#                   （对004讲代码的修改）
#  *********************************************************
'''import easygui as g
import random
secret = random.randint(1,10)
count = 3
guess = g.integerbox(msg='不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）：'\
                     ,title='数字小游戏',lowerbound=1,upperbound=10)  # lowerbound参数设置最小值，upperbound参数设置最大值
while count:
    if secret == guess:
        g.msgbox('恭喜你，猜对了！')
        break
    else:
        count -= 1
        if guess > secret:
            g.msgbox('大了，大了\n\n您还有 %d 次机会'%count)
        else:
            g.msgbox('小了，小了\n\n您还有 %d 次机会'%count)
        guess = g.integerbox(msg='不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）：'\
                     ,title='数字小游戏',lowerbound=1,upperbound=10)
    if count == 1:
        break
if count == 1:
    if secret == guess:
        g.msgbox('恭喜你，猜对了！')
    else:
        g.msgbox('还是没猜对T_T\n\n次数用完了，游戏结束')
        g.msgbox('小甲鱼心中的数字是： %d'%secret)'''

#1. 如下图，实现一个用于登记用户账号信息的界面（如果是带 * 号的必填项，要求一定要有输入并且不能是空格）。
'''import easygui as g

msg = "请填写以下信息"
title = "账号中心"
fieldNames = [" *用户名", " *真实姓名", " 固定电话", " *手机号码", " QQ", " *E-mail"]
fieldValues = [ ]
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues == None: #用户取消了炒作，则返回None
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()  # 去除首尾空格
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues) # 重新给返回的列表复制是为了再次检验错误是否出现了

print("用户资料如下：%s" % fieldValues)'''

#2.提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容。
'''import easygui as g
import os

file_path = g.fileopenbox(default = '*.txt')

with open(file_path, encoding='utf-8') as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = f.read()
    g.textbox(msg, title, text)'''

#3.在上以题的基础上增强功能：当用户点击‘OK’按钮的时候，比较当前文件是否修改过，如果修改过，则提示“覆盖保存”、“放弃保存”或“另存为...”并实现相应的功能。
'''import easygui as g
import os

file_path = g.fileopenbox(default = 'license.txt')

with open(file_path) as old_file:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = old_file.read()
    # print(text)
    text_after = g.textbox(msg, title, text)
    # print("*"*50)
    # print(text_after)
    # print("*"*50)


if text != text_after:  # [:-1]其实就是去除了这行文本的最后一个字符（换行符）后剩下的部分
    # textbox的返回值会追加一个换行符
    choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为"))
    if choice == "覆盖保存":
        with open(file_path, "w") as old_file:
            old_file.write(text_after[:-1])
    if choice == "放弃保存":
        pass
    if choice == "另存为":
        another_path = g.filesavebox(default = ".txt")
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path, "w") as new_file:
            new_file.write(text_after[:-1])'''


'''def p(s = ()):
    for i in s:
        print(i)


p((1,2,3,4,5,))'''

'''class A:
    def __init__(self,x = 0,y = 1):
        self.x = x
        self.y = y

    def printxy(self):
        print(self.x,self.y)

a = A(5,6)
a.printxy()'''

































































