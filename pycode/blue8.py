'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(200))'''
from functools import reduce

'''def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(10))
'''

'''def pmove(n,a,b,c):
    if n==1:
        move(a,c)
    else:
        pmove(n-1,a,b,c)
        move(a,c)
        pmove(n-1,b,a,c)

def move(x,y):
    print('move:%s-->%s\n'%(x,y))

A = 'A'
B = 'B'
C = 'C'
n = int(input('请输入一个数字：'))
pmove(n,A,B,C)'''


'''def trim(s):
   if len(s) == 0:
        return s
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')'''

'''def trim(s):
    if not isinstance(s,str):   #isinstance函数规定输入的必须是str字符串，其他类型会报错。
        raise TypeError('请输入字符')
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')'''


'''from collections import Iterable
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)
for ch in 'ABCSDKSW':
    print(ch)
for x,y in ([(1,1),(2,4),(3,9)]):
    print(x,y)
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))'''

'''def findMinAndMax(L):
    if L == []:
        return (None,None)
    max = L[0]
    min = L[0]
    for i in L:
        if i > max:
            max = i
        elif i < min:
            min = i
    return (min,max)       #为什么必须加一个括号才行

#findMinAndMax([5,8,3,2,9])
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''

'''L=[]
for x in range(1, 11):
    L.append(x * x)
print(L)

D = [x*x for x in range(1,11) if x%2==0]
print(D)

S = [m+n for m in 'ABC' for n in 'XYZ']
print(S)

import os
print([d for d in os.listdir('.')])

d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)'''

#L=['Helllo','World','Apple','IBM']
'''L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')'''


'''g = (x * x for x in range(10))
for n in g:
    print(n)'''
'''def fib(max):
    n,a,b,=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b #相当于t = (b, a + b) # t是一个tuple a = t[0] b = t[1]
        n=n+1
    return 'done'
print(fib(100))'''


'''def fib(max):
    n,a,b,=0,0,1
    while n<max:
        yield b   #而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。上面的函数和generator仅一步之遥。要把fib函数变成generator
        a,b=b,a+b #相当于t = (b, a + b) # t是一个tuple a = t[0] b = t[1]
        n=n+1
    return 'done'
for n in fib(100):
        print(n)
g = fib(100)
#这个循环的语法功能？
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break'''

#杨辉三角
'''def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]  #列表也可以像字符串一样合并
pass
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')'''


#coding=utf-8
#绘制蟒蛇
'''import turtle
turtle.penup()
turtle.pencolor("red")
turtle.forward(-250)
turtle.pendown()
turtle.pensize(10)
turtle.right(45)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()'''



#迭代
'''s = [x for x in range(3,31) if x % 2==0]
print(s)


print(isinstance([], Iterable))
print(isinstance((x for x in range(10)), Iterator))
for x in [1, 2, 3, 4, 5]:
    x=str(x)
    print('输出的为：'+x)


# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break'''
#高阶函数
'''def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))'''


#map() and reduce()函数
'''def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9,10])
print(r)'''

'''from functools import reduce
def add(x,y):
    return x+y
x = reduce(add,[1,3,5,7,9])
print(x)'''

#把str转换成int:如要把序列[1, 3, 5, 7, 9]变换成整数13579
'''from functools import reduce
def fn(x, y):
    return x * 10 + y
#搞不懂这个函数的功能
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

x = reduce(fn, map(char2num, '1357955825'))
print(x)'''

'''from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('1361326'))'''

'''from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('33656'))'''



'''L1 = 'adam'+'LISA'+'barT'
L2 = L1.title()
print(L2)'''

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积:
'''def normalize(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)'''

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')'''

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''def str2float(a):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return reduce(lambda x, y: x * 10 + y, map(lambda st: DIGITS[st], a.replace('.', ''))) / (
                10 ** (len(a) - a.find('.') - 1))'''

'''def str2float(s):
    a = list(map(str, s))
    for i in range(len(a)):
        if a[i] == '.':
            n = i
            c = list(map(int, a[n + 1:]))
            c.sort(reverse=True)
            return reduce(lambda x, y: x * 10 + y, list(map(int, a[:n]))) + reduce(lambda x, y: x * 0.1 + y, c) / 10
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')'''


#filter
'''def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)


def not_empty(s):
    return s and s.strip() #为什么要求交集？？？

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))'''

#用filter求素数
#计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：首先，列出从2开始的所有自然数，构造一个序列：
#2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#不断筛下去，就可以得到所有的素数。

#可以先构造一个从3开始的奇数序列(偶数序列肯定不是素数了)：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。





















































