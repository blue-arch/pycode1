#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()'''


'''class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bart = Student('Bart Simpson', 59)
bart.print_score()
def print_score(std):
    print("%s:%s" % (std.name, std.score))
print_score(bart)
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())'''


'''class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
'''

'''class Animal(object):
    def run(self):
        print('Animal is running...')
    def eat(self):
        print('Eating meat...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
def run_twice(animal):
    animal.run()
    animal.run()
dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())'''

'''class MyDog(object):
    def __len__(self):
        return 100000
dog = MyDog()
print(len(dog))'''


'''class Student(object):
    name = 'Student'
s = Student()
print(s.name)
s.name = 'michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)'''

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')'''

'''class Student(object):
    pass

s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age)
def set_score(self, score):
     self.score = score
Student.set_score = set_score
s = Student()
s.set_score(100)
s2 = Student()
print(s.score)
s2.set_score(99)
print(s2.score)'''

#使用@property
'''class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(9999)
print(s.get_score())'''

'''class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60# OK，实际转化为s.set_score(60)
print(s.score)# OK，实际转化为s.get_score()'''

'''class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth'''
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

'''class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value

    @property
    def resolution(self):
        return self._width * self._height



# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')'''

#多重继承
'''class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
'''

#定制类
'''class Student(object):
    def __init__(self,name):
        self.name = name
#怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
    def __str__(self):
        return 'Student object ()name:%s' %self.name

    __repr__ = __str__
Student.name = 'mary123'
print(Student.name)
print(Student)

s = Student('Michael')
print(s.name)#怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
print(s)'''

#__iter__
'''class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)'''

#__getitem__
'''class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):#限制了无限循环
            a, b = b, a + b
            print(a)
        return a
f = Fib()
print(f[100])
print(list(range(100))[5:80])
'''

'''class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f[10])
print(f[5:10])'''

'''class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        elif attr == 'age':
            return lambda:25
        #raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age)'''

'''class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('lanqiuwang')
print(s())
print(callable(s))'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)'''


#实现Chain().users('michael').repos输出/users/michael/repos
'''class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__

print(Chain().users('michael').repos) # /users/michael/repos

urls = Chain()    # 初始化一个实例
urls = urls.users    # 查找实例的一个属性
urls = urls('michael')   # 调用一个函数
urls = urls.repos    # 还是实例的属性'''


'''from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''

'''from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
#可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
for name, member in Weekday.__members__.items():
     print(name, '=>', member, member.value)'''


# -*- coding: utf-8 -*-
'''from enum import Enum, unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')'''


'''from enum import Enum, unique
class Color(Enum):
    red   = 1
    green = 2
    blue  = 1

print(Color.red)              # Color.red
print(Color.blue)             # Color.red
print(Color.red is Color.blue)# True
print(Color(1))               # Color.red  在通过值获取枚举成员时，只能获取到第一个成员
'''

'''alien_0 = {'color':'green','points':54}
print(alien_0['color'])
print(alien_0['points'])
alien_0['color'] = 'red'
print(alien_0['color'].lower())
alien_0['x_position'] = 360
print(alien_0['x_position'])
print(list(range(2,1100,52)))
del alien_0['color']
#print(alien_0['color'])
for key,value in alien_0.items():
    print('key:',key)
    print("value:",value)

for values in alien_0.values():
    print(values)'''

'''alien_0 = {'color':'green','points':540}
alien_1 = {'color':'red','points':35}
alien_2 = {'color':'biue','points':64}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)'''

'''aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':54,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of aliens:',len(aliens))

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']= 'yellow'
        alien['speed']='medium'
        alien['points']=10

for alien in aliens[:5]:
    print(alien)
print('...')'''

'''number = int(input("please enter a number and I'll tell you even or odd"))
if number%2==0:
    print('even')
else:
    print('the number of %s is odd'%number)'''
'''count=1
while count<=100:
    print(count)
    count+=1
'''
'''prompt = 'please enter a word'
prompt+='\nor enter quit to get out'

while 1:
    message = input(prompt)
    if message=='quit':
        break
    else:
        print(message)'''

'''count=0
while count <10000:
    count += 1
    if count%5==0:
        continue
    print(count)'''

'''uncon=['wfwef','wfef','wefwef','rtehth','ehtheh']
con=[]
while uncon:
    cur=uncon.pop()
    print('verfied num :'+cur)
    con.append(cur)

for i in con:
    print(i.title())'''

'''responses={}
poll = True
while poll:
    name = input('invester name')
    rep = input('which mountain do youwant to climb:')

    responses[name] = rep
    repeat = input('do you want to continue now yes or no')
    if repeat=='no':
        poll = False

print('\npollresults')
for name,rep in responses.items():
    #print(name+" want to climb "+rep)
    print("%s want to climb %s!"%(name,rep))'''


'''def build_person(first_name,last_name,age=''):
    person = {'first' : first_name , 'last' : last_name}
    if age:
        person['age'] = age
    return person

person1 = build_person('lan','qiuwang',age = 23)

print(person1)'''

'''def get_name(first_name,last_name):
    full_name = first_name +' '+ last_name
    return full_name

while True:
    print('\nplease enter your name:')
    print('\nyou can enter q to quit out!')
    f_name = input('please enter your first name:')
    if f_name == 'q':
        break
    l_name = input('please enter your last name:')
    if l_name == '':
        break
    name = get_name(f_name,l_name)
    print('hello %s!'%name)'''


















































































































