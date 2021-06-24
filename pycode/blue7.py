'''def pow(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print(pow(5,5))'''

'''def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([1,2]))
print(add_end([1,2,3]))'''

'''def cal(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(cal(5,6))
'''

'''def person(name, age, **kw):
    print('name:', name, 'age:',age,'other:', kw)
print(person('Bob', 35, city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))'''



#输入为空时要求报错
def product(x,*numbers):
    s = x
    for n in numbers:
        s = s * n
    return s
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')









