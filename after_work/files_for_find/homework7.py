

'''class try_int(int):
    def add(self,other):
        return int.__sub__(self,other)

    def sub(self,other):
        return int.__add__(self,other)

a = try_int(3)
b = try_int(5)
print(a + b)'''


'''class int(int):
    def add(self,other):
        return int.__sub__(self,other)

    def sub(self,other):
        return int.__add__(self,other)

a = int('3')
b = int(8)
print(a + b)'''

#__radd__属性
#右加：当左边没有实现add属性时，看右边又没有radd属性，如有右边又radd属性则调用此属性进行右加
'''class A:

    def __init__(self,name,age=20):
        self.name = name
        self.age = age

    def __add__(self, other):
        self.age += other.age
        return self

    def __iadd__(self, other):
        return A(self.name,self + other)

    def __radd__(self, other):
        if hasattr(other,'age'):
            return A(self.age + other.age)
        else:
            try:
                x = int(other)
            except:
                x = 100
            self.age = self.age + x
            return self.age

tom = A('tom')
ss = A('ss')
print(ss + tom)'''
#print('ss'+tom)     #因为字符串没有add方法，所以调用tom的右侧radd，进行计算

'''class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self,other)

a = Nint(5)
b = Nint(3)
print(a+b)
print(int(12)+b)'''

'''class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(self,other)

a = Nint(5)
b = Nint(8)
print(a-b)
print(3-b)
print(b-3)
'''

#简单定制
'''class A:
    def __str__(self):
        return "蓝求旺是帅哥！"
    def __repr__(self):
        return "阿里拉起来哇哇"
a = A()
print(a)'''
'''class B:
    def __repr__(self):
        return "阿里拉起来哇哇"
b = B()
print(b)
'''
#第四十四课：魔法方法：简单定制（计时器的类）
#简单定制：
'''import time as t
class MyTimer():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.star = 0
        self.sto = 0

    def __str__(self):
        return self.prompt     #当_calc方法没有运行时，表明prompt变量根本没有定义，最好还是在__init__中先定义好！

    __repr__ = __str__
    #不继承int,str...类还可以用add?????
    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    #开始计时
    def start(self):
        self.star = t.localtime() #返回的是一个（含有六个元素）元组
        self.prompt = '提示，请先调用stop()停止计时'
        print('计时开始...')

    def stop(self):
        if not self.star:
            self.prompt = '提示，请先调用start()开始计时'
        else:
            self.sto = t.localtime()
            self._calc()
            print('计时结束！')

    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.sto[index] - self.star[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
                #这里的加不影响，因为调用的是str的加的魔法方法
        #print(self.prompt)
        self.star = 0
        self.stop = 0
        self.lasted = []
        
t1 = MyTimer()
t1.start()
t1.stop()
print(t1)'''

#0.按照课堂中的程序，如果开始计时的时间为（2022年2月22日16:30:30），停止时间是（2025年1月23日15:30:30），那按照我们用停止时间减去开始时间的计算方式就会出现负数，你应该对此做一些转换。

'''import time as t
class MyTimer():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.borrow = [1,12,31,24,60,60]
        self.prompt = '未开始计时'
        self.lasted = []
        self.star = 0
        self.sto = 0

    def __str__(self):
        return self.prompt     #当_calc方法没有运行时，表明prompt变量根本没有定义，最好还是在__init__中先定义好！

    __repr__ = __str__

    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    #开始计时
    def start(self):
        self.star = t.localtime() #返回的是一个（含有六个元素）元组
        self.prompt = '提示，请先调用stop()停止计时'
        print('计时开始...')

    def stop(self):
        if not self.star:
            self.prompt = '提示，请先调用start()开始计时'
        else:
            self.sto = t.localtime()
            self._calc()
            print('计时结束！')

    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            #self.lasted.append(self.sto[index] - self.star[index])      #这里出现了负号，需要解决
            #if self.lasted[index]:
            #    self.prompt += (str(self.lasted[index]) + self.unit[index])
            temp = self.sto[index] - self.star[index]
            if temp < 0:
                # 测试高位是否有得借，没得借的话再向高位借……
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-1] += self.borrow[index-i] - 1 #
                    self.lasted[index-i-1] -= 1                      #这里代码有问题。。。。。。。。。。。。。。。。。
                    i+=1                                             #
                self.lasted.append(self.borrow[index] + temp)        #
                self.lasted[index-1] -= 1          #这里要减一是因为跳出了while循环，或者没进入循环，被借位后的那位要减一
            else:
                self.lasted.append(temp)

        self.star = 0
        self.stop = 0
        #self.lasted = []          #妈蛋，弹幕里提的建议也不能全信。。。。。。。。。。。。。。。。。
        print(self.prompt)
t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(65)
t1.stop()
t2.start()
t.sleep(15)
t2.stop()
print(t1 + t2)
'''

#1.相信大家已经意识到不对劲了：为毛一个月一定是31天？不知道可能也是30天或者29天吗？（上一题我们的答案是假设一个月31天）。没错，如果要正确得到月份的天数，我们还需要考虑是否闰年，还有每月的最大天数，所以太麻烦了……如果我们不及时就在，我们会在错误的道路上越走越远……
#所以，这一次，小甲鱼提出了更优秀的解决方案（Python官方推荐）：用time模块的perf_counter()和process_time()计算，其中perf_counter()返回计时器的精准时间（系统的运行时间）；process_time()返回当前进程执行CPU的时间总和。
#题目：改进我们课堂中的例子，这次使用perf_counter()和process_time()作为计时器，另外新增一个set_time()方法，用于设置默认计时器（默认是perf_counter()，可以通过此方法修改为process_time() ）。
'''
import time as t
class MyTimer():
    def __init__(self):
        self.prompt = '未开始计时'
        self.lasted = []
        self.star = 0
        self.sto = 0

    def __str__(self):
        return self.prompt     #当_calc方法没有运行时，表明prompt变量根本没有定义，最好还是在__init__中先定义好！

    __repr__ = __str__

    def __add__(self, other):

        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" % result
        return prompt

    #开始计时
    def start(self):
        self.star = self.default_timer()
        self.prompt = '提示，请先调用stop()停止计时'
        print('计时开始...')

    def stop(self):
        if not self.star:
            self.prompt = '提示，请先调用start()开始计时'
        else:
            self.sto = self.default_timer()
            self._calc()
            print('计时结束！')

    def _calc(self):
        self.lasted = self.sto - self.star
        self.prompt = print('总共运行了%0.2f秒'%self.lasted)
        #print(self.prompt)
        self.star = 0
        self.stop = 0
        #self.lasted = []          #妈蛋，弹幕里提的建议也不能全信。。。。。。。。。。。。。。。。。


    def set_timer(self,timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效")

t1 = MyTimer()
t1.set_timer('perf_counter')
t1.start()
t.sleep(5.2)
t1.stop()
t2 = MyTimer()
t2.set_timer('perf_counter')
t2.start()
t.sleep(5.2)
t2.stop()
print(t1 + t2)'''


#2.既然咱都做到了这一步，那不如再深入以下，再次改进我们的代码，让它能够统计一个函数运行若干次的时间。
#要求一：函数调用的次数可以设置（默认是1000000次）
#要求二：新增一个timing()方法，用于启动计时器

'''import time
a1=time.perf_counter()
a2=time.process_time()
c=1
for i in range(1,20000):
    c*=i
b1=time.perf_counter()
b2=time.process_time()
print(b1-a1,'s')
print(b2-a2,'s')'''

'''import time as t
class MyTimer():
    def __init__(self, func, number=1000000):
        self.prompt = '未开始计时'
        self.default_timer = t.perf_counter
        self.func = func
        self.number = number
        self.lasted = 0.0
        self.star = 0
        self.sto = 0

    def __str__(self):
        return self.prompt     #当_calc方法没有运行时，表明prompt变量根本没有定义，最好还是在__init__中先定义好！

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" % result
        return prompt

    def timing(self):
        self.star = self.default_timer()
        for i in range(self.number):
            self.func()
        self.sto = self.default_timer()
        self.lasted = self.sto - self.star
        self.prompt = "总共运行了 %0.2f 秒" % self.lasted
        #return self.prompt

    def set_timer(self,timer):
        if timer == 'process_time':               #time.perf_counter()
            self.default_timer = t.process_time   #返回性能计数器的值（以分秒为单位），即具有最高可用分辨率的时钟，以测量短持续时间。它包括在睡眠期间和系统范围内流逝的时间。返回值的参考点未定义，因此只有连续调用结果之间的差异有效。
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter   #process_time是cpu有效运行时间，空闲时间不算
        else:
            print("输入无效")

def test():
    text = 'i love faffgv qag aqg ag qag hhhhqa'
    char = 'o'
    if 'o' in text:
        pass

t1 = MyTimer(test)
t1.timing()
print(t1)
t2 = MyTimer(test, 100000000)
t2.timing()
print(t2)'''

'''class B:
    def __init__(self,func):
        self.func = func
    def p(self):
        self.func()
        #test()

def test():
    print('a')

b = B(test)
b.p()'''

'''#导入timeit.timeit
from timeit import timeit

#看执行1000000次x=1的时间：
print(timeit('x=1'))

#看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
print(timeit('x=1', number=1))

#看一个列表生成器的执行时间,执行1次：
print(timeit('[i for i in range(10000)]', number=1))

#看一个列表生成器的执行时间,执行10000次：
print(timeit('[i for i in range(100) if i%2==0]', number=10000))'''

'''from timeit import timeit

def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=1000)
print(t)'''


'''class Rectangle:                            #默认继承obj类

    def __init__(self, longth = 0,width = 0):
        self.longth = longth                  #赋值时都会触发setattr方法
        self.width = width

    def __setattr__(self, name, value):
        if name == 'square':
            self.longth = value               #此处不会无限递归，因为第二次递归会跳到else语句里面去
            self.width = value
        else:
            super().__setattr__(name,value)   #我就知道要用super找超类使用它就不会发生无限递归了
            #self.__dict__[name] = value      #相当于调用了字典方法

    def getArea(self):
        return self.longth * self.width

r1 = Rectangle(4,5)
print(r1.getArea())
r1.square = 10           #传入square了，自动触发setattr方法
print(r1.longth,r1.width,r1.getArea())'''


'''def calc(a, b, c):
    return (a + b) * c

a = calc(1, 2, 3)
b = calc([1, 2, 3], [4, 5, 6], 2)
c = calc('love', 'FishC', 3)
print(a)
print(b)
print(c)
'''
#第四十二课：魔法方法：算术运算
#0.我们都知道在Python中，两个字符串相加会自动拼接字符串，但遗憾的是两个字符串相减却抛出异常，因此，现在我们要求定义一个Nstr类，支持字符串的相减操作：A - B，从A中去除所有B的子字符串。

'''class Nstr(str):

    def __sub__(self, other):
        return self.replace(other,'')

a = Nstr('I love fish ciiiiiiiiiiiiiiii')
b = Nstr('i')
print(a - b)
'''

#1.移位操作符是应用于二进制操作数的，现在需要你定义一个新的类Nstr，也支持移位操作符的运算。

'''class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]  # 感觉代码有问题


a = Nstr('I love FishC.com!')
print(a << 3)
print(a >> 3)'''


#2.定义一个类Nstr，当该类的实例对象间发生的加、减、乘、除运算时，将该对象的所有字符串的ASCII码之和进行运算。

'''class Nstr:
    def __init__(self,arg = ''):
        if isinstance(arg,str):
            self.total = 0
            for i in arg:
                self.total += ord(i)
        else:
            print('传入的不是字符串，参数错误')

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total

a = Nstr('abc')
b = Nstr('def')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)'''

#第四十三课：魔法方法：反运算


#2.请问如何在继承的类中调用基类的方法？
'''class A(object):
    def __init__(self, a=0):
        self.a = a
    def get(self):
        return self.a

class B(A):
    def __init__(self, b):
        super(B, self).__init__(b)
    def get(self):
        return super(B, self).get()

if __name__ == '__main__':
    b = B(10)
    print(b.get())'''

#5.尝试自己列举说明如何使用类中的静态方法，并指出使用静态方法有什么不同和哪些需要注意的地方？
'''class C:
    @staticmethod
    def static(arg1, arg2, arg3):
        print(arg1, arg2, arg3, arg1 + arg2 + arg3)

    def nostatic(self):
        print("I'm the fucking normal method!")

c = C()
c.static(1, 2, 3)
c.nostatic()'''

#0.定义一个类，当实例化该类的时候，自动判断传入了多少个参数，并显示出来。

'''class C:
    def __init__(self,*arg):
        if not arg:
            print('没有传入参数')
        else:
                print('传入了%d个参数,分别是'%(len(arg)),end = '')
                print(arg)

c = C(1,2,'i',4,'蓝求旺')
'''

#1.定义一个单词（Word）类继承自字符串，重写比较操作符，当两个Word类对象进行比较时，根据单词的长度来进行比较大小。
#加分要求：实例化时如果传入的是带空格的字符串，则取第一个空格前的单词作为参数。

'''class Word(str):
    def __new__(cls,word):
        # 注意我们必须要用到__new__方法，因为str是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print("Value --%s-- contains spaces. Truncating to first space."%word)
            word = word[:word.index(' ')] # 单词是第一个空格之前的所有字符
        return str.__new__(cls,word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return  len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

w1 = Word('abcd')
w2 = Word('abca vsdv')
if w1 >= w2:
    print(True)'''


#第四十五课：魔法方法：属性访问
#2.在不上机验证的情况下，你能推断以下代码会显示什么吗？
'''class C:
    def __getattr__(self, name):
        print(1)
    def __getattribute__(self, name):
        print(2)
    def __setattr__(self, name, value):
        print(3)
    def __delattr__(self, name):
        print(4)

c = C()
c.x = 1
print(c.x)'''


'''class C:
    def __getattr__(self, name):
        print(1)
        return super().__getattr__(name)

    def __getattribute__(self, name):
        print(2)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print(3)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(4)
        super().__delattr__(name)

c = C()
#c.x
print(dir(super))
'''
#4.请指出以下代码的问题所在：
'''class Counter:
    def __init__(self):
        self.counter = 0  # 这里会触发__setattr__调用
    def __setattr__(self, name, value):
#既然需要__setattr__调用才能真正设置self.counter的值，所以这个时候self.counter还没有定义，所以没法+1，错误的根源
        self.counter += 1
    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)'''
#正确做法
'''class Counter:
    def __init__(self):
        self.counter = 0
    def __setattr__(self, name, value):
        super().__setattr__(name, value+1)
    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)'''

#0.按要求重写魔法方法：访问一个不存在的属性时，不报错并且提示“该属性不存在！”

'''class Demo:
    def __getattr__(self):
        return "该属性不存在"

d = Demo()
d.x'''

#1.编写Demo类，使得下边代码可以正常运行：
'''class Demo:
    def __getattr__(self,name):
        self.name = 'fishc'
        return self.name

demo = Demo()
print(demo.x)
demo.x = "X-man"
print(demo.x)'''

#不能用该方法，应为只有设置属性的时候才会调用setattr
'''class Demo:
    def __setattr__(self,name,value = 'fishc'):
        self.name = value
        super().__setattr__(name,value)
        #return self.name

demo = Demo()
print(demo.x)
demo.x = "X-man"'''

#2.修改上班第4题，使之可以正常运行；编写一个Counter类，用于实时检测对象有多少个属性。

'''class Counter:
    def __init__(self):
        super().__setattr__('counter', 0)
    def __setattr__(self, name, value):
        super().__setattr__('counter', self.counter+1)
    def __delattr__(self, name):
        super().__setattr__('counter', self.counter-1)
        super().__delattr__(name)

c = Counter()
c.x = 1
print(c.counter)
del c.x
print(c.counter)'''


#这个类相当于做一些默认的操作
'''class Ce:
    def __init__(self,value = 26):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)
#真正的具体操作在这个类中进行
class Fa:
    def __get__(self, instance, owner):
        return instance.ce*1.8+32
    def __set__(self, instance, value):
        instance.ce = (float(value) - 32)/1.8

class Temperature:
    ce = Ce()
    fah = Fa()
'''

#第四十六课：魔法方法：描述符（property的原理）
#0.按要求编写描述符MyDes：当类的属性被访问、修改或设置的时候，分别作出提醒。
'''class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.name

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.name = value

    def __delattr__(self, instance):
        print("正在删除变量：", self.name)
        print("┗|｀O′|┛ 嗷~~这个变量没法删除~")'''

#1.按要求编写描述符MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件。
'''import time

class Record:
    def __init__(self, initval=None, name='x'):
        self.val = initval
        self.name = name
        self.filename = "record.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        filename = "%s_record.txt" % self.name
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(value)))
        self.val = value'''

#2.编写描述符MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle的文件中。如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。
'''import os
import pickle

class MyDes:
    saved = []

    def __init__(self, name='11'):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)

class Test:
    x = MyDes()

test = Test()
test.x = 10'''





#生成器
'''def mygun():
    print('生成器执行')
    yield 1
    yield 2

a = mygun()
print(next(a))
print(next(a))'''

'''def fib():
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        yield a

a = fib()
print(next(a))
print(next(a))
print(next(a))
for i in range(100):
    print(next(a))
for i in fib():
    if i >100000:
        break
    print(i,end = ' ')

print(list(filter(lambda x:x%2,range(10))))'''

'''def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

fib(6)'''

#还可以通过yield实现在单线程的情况下实现并发运算的效果
#太难了算了。。。。
'''import time
def consumer(name):
    print("%s 准备学习啦!" % name)
    while True:
        lesson = yield

        print("开始[%s]了,[%s]老师来讲课了!" % (lesson, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(10):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i)
        c2.send(i)'''

'''for i in range(10):
    lambda i: 2 * i + 1'''


#素数
'''import math
def isprime(n):
    if n<= 1:
        return True
    for i in range(2,n):
        if n % i == 0:
            print('不是素数')
            break
        if i == n-1:
            print('是素数')

isprime(100)'''

#10以内的素数之和是：2+3+5+7=17，那么请编写程序，计算2000000以内的素数之和？
#如果你的想法是将2000000以内的所有素数都找到并存放到一个列表中，再依次进行求和计算，那么这个列表极有可能会撑爆你的内存，所以这道题就必须用到生成器去实现。

'''import math

def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2==0:
            return False
        for i in range(3,int(math.sqrt(num))+1,2):
            if num%i == 0:
                return False
        return True
    return False

def get_prime(num):
    while True:
        if is_prime(num):
            yield num

        num+=1

def solve():
    sum = 2
    for next_prime in  get_prime(3):
        if next_prime < 2000000:
            sum = sum + next_prime
        else:
            print(sum)
            return



if __name__ == '__main__':
    solve()
'''


#算法改进:1000内素数
#

'''import math
def list_prime(n):
    b = []
    for a in range(2,n):
        if a%2!=0:
            b.append(a)
    for d in b:
        for i in range(3,int(math.sqrt(d))+1,2):
            if d % i==0:
                b.remove(d)
                break
    return [2] + b


b = list_prime(200000)
sum = 0
for i in b:
    sum += i
print(sum)
'''

#再改进





































