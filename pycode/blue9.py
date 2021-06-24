#1000以内的素数
'''def odd_enter():
    n = 1
    while True:
        n = n+2
        yield n

def odd_ok(x):
    return lambda x:x%n>0

def primer():
    yield 2
    it = odd_enter
    while True:
        n = next(it)
        yield n
        it = filter(odd_ok,it)

for n in primer():
    if n < 1000:
        print(n)
    else:
        break'''
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''def is_palindrome(n):
    m = str(n)
    m = str(n)
    if m == m[::-1]:  # 使用字符串翻转的形式（切片）
        return True
    else:
        return False'''
'''def is_palindrome(n):
    m = str(n)
    if len(m)==1:
        return True
    else:
        for i in range(len(m)//2):
            if m[i] != m[-i - 1]:
                return False
        return True

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')'''

#sorted函数
'''L=sorted([36, 5, -12, 9, -21], key=abs)#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：
print(L)
s = sorted(['bob', 'about', 'Zoo', 'Credit'])#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(s)
t = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(t)
x = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(x)
name = ['bob', 'about', 'Zoo', 'Credit']
name.reverse()
print(name)#不能print(name.reverse())?????'''


#请用sorted()对上述列表分别按名字排序：关键在于把列表中的元素取出来
'''L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
#key函数作用于序列的每一个元素，这里的元素就是每一个元组，因此思路就是去除元组中需要进行比较的部分：如姓名或者年纪
def by_grade(n):
    return n[1]
def by_name(t):
    for x in t:
        if isinstance(x,str):
            return x
    pass
def by_score(t):
    for x in t:
        if isinstance(x,int):
            return -x
    pass
L2 = sorted(L, key=by_grade)
print(L2)'''

#闭包
'''def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
f1 = lazy_sum(1, 3, 5, 7, 9)
print(f(),f1())'''


#利用闭包返回一个计数器函数，每次调用它返回递增整数：
#first利用生成器
'''def createCounter():
    def plus():
        n = 1
        while True:
            yield n
            n += 1
    x = plus()
    def counter():
        return next(x)
    return counter'''
#second利用闭包函数外函数中的变量
'''def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')'''

'''x = "'hello world'"
def func():
    global x
    print(x)
    x = 'hello main1'
    print('func',x,id(x))
x='hello'
func()'''

#匿名函数
'''def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
print('=======================================================================')
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)'''

#装饰器
'''def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()'''
#now = log(now)由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。



'''def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()'''
# now = log('execute')(now)
#我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
#以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

'''def log(func):
    def wrapper(*args,**kw):
        print('call%s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-2-22')

now()'''

#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time,functools
'''def metric(fn):
    @functools.wraps(fn)
    def log(*args,**kw):
        print('fn():%s' % time.ctime())  # (这里可以不用加)
        print(fn(*args,**kw))
    return log'''

'''def metric(fn):
    def wrapper(*args, **kw):
        start_time = time.time()
        x = fn(*args, **kw)#为什么要调用fn
        end_time = time.time()
        #exe_time = (end_time - start_time) * 1000
        print('%s executed in %s ms' % (fn.__name__, end_time-start_time))
        return x
        #t1 和 t2 之间调用了fn函数，wrapper中 return 的时候又调用了 fn 函数，这里是有点问题的。t1 t2之间的 fn 调用的结果应该用一个变量存起来，然后 return 这个变量的值。你现在这样是造成了额外的调用~
    return wrapper
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y;
@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z;
f=fast(11,22)
s=slow(11,22,33)
if f !=33:
    print('测试失败')
elif s!=7986:
    print('测试失败')'''

#偏函数
#x进制转换成10进制
'''def int2(x, base=2):
    return int(x, base)
print(int2('1010010101010101001111010'))'''

'''import functools
int2 = functools.partial(int, base=2)
print(int2('1010010101010101001111010'))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
'''




































































































































































































