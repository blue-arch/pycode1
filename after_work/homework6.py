#第三十六课：类和对象：给大家介绍对象
#0.按照以下提示尝试定义一个Person类并生成实例对象。
#属性：姓名（默认姓名为“小甲鱼”）
#方法：打印姓名
#提示：方法中对属性的引用形式需加上self，如self.name

'''class Person:
    name = '小甲鱼'

    def printName(self):
        print(self.name)'''

#1.按照以下提示尝试定义一个矩形类并生成类实例对象。
'''class Rectangle:
    length = 5
    width = 4

    def setRect(self):
        print("请输入矩形的长和宽")
        self.length = float(input("长："))
        self.width = float(input("宽："))

    def getRect(self):
        print("这个矩形的长是：%.2f，宽是：%.2f" % (self.length, self.width))

    def getArea(self):
        return self.length * self.width'''

# 第三十七课：类和对象：面向对象编程
# 0.按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
#平日票价100元
#周末票价为平日的120%
#儿童半票
'''class Ticket:

    def __init__(self,weekend = False,child = False):
        self.price = 100
        if weekend:
            self.increase = 1.2
        else:
            self.increase = 1

        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self,num):
        return self.price * self.increase * self.discount * num

adult = Ticket()
child = Ticket(child = True)
print("2个大人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))

adult2 = Ticket(weekend=True)
child2 = Ticket(weekend=True, child=True)
print("2个大人 + 1个小孩周末票价为：%.2f" % (adult2.calcPrice(2) + child2.calcPrice(1)))'''


#1.游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。（初学者不一定可以完整实现，但请务必先自己动手，你会从中学到很多）
'''游戏场景为范围(x,y)为 0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力为2(可以随机选择1还是2),鱼儿的最大移动能力为1
当移动到场景边缘,自动向反方向移动 ????           以x=0和x=10对称
乌龟初始化体力为100（上限）
乌龟每移动一次,体力消耗1
当乌龟和鱼坐标重叠,乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0(挂掉)或鱼儿的数量为0游戏结束
答：代码如下：'''
'''import random as r

class Turtle:
    def __init__(self):
        self.power = 100
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = self.x + r.choice([-1, -2, 1, 2])
        new_y = self.y + r.choice([-1, -2, 1, 2])
        if new_x<0:
            self.x = 0 - new_x

        elif new_x>10:
            self.x = 20 - new_x
        else:
            self.x = new_x
        if new_y < 0:
            self.y = 0 - new_y

        elif new_y > 10:
            self.y = 20 - new_y
        else:
            self.y = new_y
        self.power -= 1
        return (self.x ,self.y)
    def eat(self):
        self.power += 20
        if self.power>100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = self.x + r.choice([-1,1])
        new_y = self.y + r.choice([-1, 1])
        if new_x < 0:
            self.x = 0 - new_x

        elif new_x > 10:
            self.x = 20 - new_x
        else:
            self.x = new_x
        if new_y < 0:
            self.y = 0 - new_y

        elif new_y > 10:
            self.y = 20 - new_y

        else:
            self.y = new_y
        return (self.x, self.y)
turtle = Turtle()
t = []
for i in range(10):
    fish = Fish()
    t.append(fish)
while True:
    if not turtle.power:
        print('乌龟死了！')
        break

    if not t: # len(t) == 0
        print('乌龟死了！')
        break

    print('乌龟没移动前坐标（%d,%d）'%(turtle.x,turtle.y))
    turtle.move()
    print('乌龟没移动后坐标（%d,%d）' % (turtle.x, turtle.y))
    for fish in t:
        print('鱼移动前的坐标为：(%d,%d）' % (fish.x, fish.y))
        fish.move()
        print('鱼移动后的坐标为：(%d,%d）'%(fish.x,fish.y))
        if turtle.x == fish.x and turtle.y == fish.y:
            turtle.eat()
            t.remove(fish)
            print('吃了鱼之后的体力为：%d'%turtle.power)'''



'''import random as r

class Turtle:
    def __init__(self):
        #初始体力
        self.power = 100
        #初始位置
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        # 随机计算方向并移动到新的位置(x, y)
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
            # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
            self.y = 10 - (new_y - 10)
        elif new_y > 10:
        else:
            self.y = new_y
            # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)  #以元组形式返回

    def eat(self):
        self.power += 20
        if self.power > 20:
            self.power = 100

class Fish:
    def __init__(self):
        # 初始位置随机
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        # 随机计算方向并移动到新的位置(x, y)
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼都吃完了，游戏结束！")
        break

    if not turtle.power:
        print("乌龟体力耗尽，挂了！")
        break

    #游戏开始！
    #首先乌龟迈出第一步
    print("乌龟移动前坐标：", (turtle.x, turtle.y))  # 乌龟移动前
    turtle.move()
    print("乌龟移动后坐标：", (turtle.x, turtle.y))  # 乌龟移动后
    for item in fish:
        print("鱼移动前坐标：", (item.x, item.y))
        item.move()  # 感觉鱼的移动前后的坐标差有问题
        print("鱼移动后坐标：", (item.x, item.y))
        if item.x == turtle.x and item.y == turtle.y:
            turtle.eat()
            fish.remove(item)
            print("死了一只鱼")
            print("乌龟最新体力值为 %d" % turtle.power)'''


#第三十八课：类和对象：继承
#5.多重继承使用不当会导致重复调用（也叫钻石继承、菱形继承）的问题，请分析以下代码在实际编程中有可能导致什么问题？
'''---> B ---
A --|          |--> D
     ---> C ---'''
#使用 super() 可以很好地避免构造函数被调用两次。
'''class A():
    def __init__(self):
        print("进入A...")
        print("离开A...")

class B(A):
    def __init__(self):
        print("进入B...")
        A.__init__(self)
        print("离开B...")

class C(A):
    def __init__(self):
        print("进入C...")
        A.__init__(self)
        print("离开C...")

class D(B, C):
    def __init__(self):
        print("进入D...")
        B.__init__(self)
        C.__init__(self)
        print("离开D...")

d = D()'''

#6.如何解决上一题中出现的问题？
#class A():   class A:
'''class A(object):
    def __init__(self):
        print("进入A...")
        print("离开A...")

class B(A):
    def __init__(self):
        print("进入B...")
        super().__init__()
        print("离开B...")

class C(A):
    def __init__(self):
        print("进入C...")
        super().__init__()
        print("离开C...")

class D(B, C):
    def __init__(self):
        print("进入D...")
        super().__init__()
        print("离开D...")

d = D()'''

#0.定义一个点（Point）类和直线（Line）类，使用getLen方法可以获得直线的长度。
#提示：
#设点A(X1,Y1)、B(X2,Y2)，则两点构成的直线长度为|AB| = √(X1-X2)^2 + (Y1-Y2)^2
#Python中计算开根号可使用math模块中的sqrt函数
#直线需有两点构成，因此初始化时需要有两个点（Point）对象作为参数

'''import math
class Point:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line:
    def __init__(self):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()
        self.len = math.sqrt(self.x*self.x + self.y*self.y)

    def get_len(self):
        return self.len

p1 = Point(1,2)
p2 = Point(3,4)
l = Line()
print(l.get_len())'''

'''import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line():
    def __init__(self, p1, p2):      #此处有点不同，是传实例参数。。。。。。。。
        self.x = p1.getX() - p2.getX()        
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def getLen(self):
        return self.len

p1 = Point(1, 1)
p2 = Point(1, 4)
line = Line(p1, p2)
print(line.getLen())'''

#第三十九课：类和对象：组合
#组合：Python继承机制很有用，但容易把代码复杂化以及依赖隐含继承。因此，经常的时候，我们可以使用组合来代替。在Python里组合其实很简单，直接在类定义中把需要的类放进去实例化就可以了。

# 乌龟类
'''class Turtle:
    def __init__(self, x):
        self.num = x

# 鱼类
class Fish:
    def __init__(self, x):
        self.num = x

# 水池类
class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)  # 把乌龟类实例化组合进来
        self.fish = Fish(y)      # 把鱼类实例化组合进来

    def print_num(self):
        print("水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.print_num()
print(dir(Pool))'''


#0.思考这一讲学习的内容，请动手在一个类中定义一个变量，用于跟踪类有多少个实例被创建（当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）。
'''class C:
    count = 0
    def __init__(self):
        C.count += 1

    def __del__(self):
        C.count -= 1
a = C()
b = C()
c = C()
del a
del b
print(c.count)'''


#1.定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特征的数据结构。至少需要有以下办法：
#方法名              含义
#isEmpty()	判断当前栈是否为空（返回True或False）
#push()	    往栈的顶部压入一个数据项
#pop()	    从栈顶弹出一个数据项（并在栈中删除）
#top()	    显示当前栈顶的一个数据项
#botton()	显示当前栈底的一个数据项

'''class Stack:
    def __init__(self,start = []):     #???????????????????????????????????????
        self.stack = []                 #两个列表，一个用来存储传入的数据，另一个用来作为类里面的各种操作！
        #for i in start:               #更函数一样的
            #self.push(i)           #类里调用自己的方法

    def isEmpty(self):            #为空则返回True
        return not self.stack

    def push(self,obj):
        print('成功入栈数据：',obj)
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            print('成功出栈数据：',self.stack[-1])
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            print('栈顶数据：',end = '')
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            print('栈底数据：',end = '')
            return self.stack[0]

    def showStack(self):
        print('目前栈内所有数据为：',end = '')
        return self.stack[:]

#s = Stack([1,2,3,4,5])
s = Stack([])
print(s.isEmpty())  # True
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
print(s.showStack())
print(s.top())  # 栈顶是5
s.pop()  # 5被弹出，栈顶变成4
print(s.showStack())
print(s.top())
print(s.bottom())
'''

#0.小李做事常常丢三落四的，写代码也是一样，常常打开文件又忘记关闭。你能不能写一个FileObject类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭？
'''class FileObject:
    #给文件对象进行包装从而确认在删除时文件流关闭
    def __init__(self,filename = 'sample.txt'):
        # 读写模式打开一个文件
        self.new_file = open(filename,'r+')
    def __del__(self):
        self.new_file.close()
        del self.new_file


a = FileObject()'''

#1.按照以下要求，定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度=摄氏度*1.8+32）

'''class CtoF(float):

    def __new__(cls, arg = 0):
        #return 1.8 * arg + 32
        return float.__new__(cls, arg * 1.8 + 32)

a = CtoF(38)
print(a)
print(type(a))'''



#2.定义一个类继承于int类型，并实现一个特殊功能：当传入的参数是字符串的时候，返回该字符串中所有字符的ASCII码的和（使用ord()获取一个字符的ASCII码值）。

'''class Nint(int):
    def __new__(cls, arg = 0):
        if isinstance(arg,str):
            total = 0
            for i in arg:
                total += ord(i)
            arg = total
        return int.__new__(cls,arg)

print(Nint('bb'))
'''

'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


a = fib(10)
print(next(a))
print(next(a))
print(next(a))
'''








































