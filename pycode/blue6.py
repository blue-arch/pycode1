'''s1 = 72
s2 = 85
a = ((s2-s1)/s1)*100
''''''print('小明成绩提升了：%02.2f%%'%a)
print('%03d-%03d' % (3, 1))
print('%2.4f' % 3.1415926)
print('小明成绩从去年的%d分提升到今年的%d分,提升的百分点是：%.1f%%' %(s1,s2,a))
print('小明成绩从去年的{0}分提升到今年的{1}分,提升的百分点是：{2:.1f}%'.format(s1,s2,a))'''
'''classmates = ['mary','chod','ajf']
print(classmates[0])
a = len(classmates)
print(a)'''
'''s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))'''
'''classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop(0)
classmates[0] = 'mary'
print('classmates =', classmates)
print(len(classmates))'''
'''age = 20
if age > 18:
    print('your age is :',age)
else:
    print('adults')'''
'''age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')'''
'''birth = int(input('your birth:'))
if birth >= 2000:
    print('00后')
else:
    print('00前')'''
'''height = float(input('your height(m):'))
weight = float(input('your weight(kg):'))
bmi = weight/(height*height)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')'''
names = ['Michael', 'Bob', 'Tracy']
'''for name in names:
    print(name)
    sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)'''
'''sum = 0
for x in range(101):
    sum = sum + x
    print(x)
print(sum)'''
'''sum = 0
n=99
while n>0:
    sum = sum+n
    n = n-2
print(sum)'''
'''L = ['Bart', 'Lisa', 'Adam']
n=3
while n > 0:
    print('hello %s'%L[n-1])
    n=n-1'''
'''n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')'''
'''L = ['Bart', 'Lisa', 'Adam']
for everyname in L:
	print('hello',everyname)'''
'''d = {'michael':95,'bob':60,'mary':29}
print(d.values())
dict = {'Name': 'Zara', 'Age': 7}
print( "Value : %s" %  dict.values())'''

'''n=0
sum=0
while n<=100:
    sum=sum+n
    n=n+1
else:
    print('sum=',sum)

n=1
sum=0
while n<=100:
    sum=sum+n*n+1
    n=n+1
else:
    print('sum=',sum)'''


'''n=123
m=234
di={"n":n,"m":m}
for i in di.keys():
    print(hex(di[i]))
L=[123,234]
print("first:%s\nsecond:%s" %(hex(L[0]),hex(L[1])))'''
'''n1 = hex (int(input("请输入第一组数字：")))
n2 = hex(int(input("请输入第二组数字：")))
print ("第一组转换为16进制为:%s\n第二组为：%s" % (n1,n2))'''

#x = input('please input a number:')
'''def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else :
        return -x
print(my_abs('a')'''

'''import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(r)
#print(x,'\n',y)'''

import math
def quadratic(a,b,c):
    if b*b < 4*a*c:
        print('测试失败')
        return '无解'             #怎么跳出来？
    else:
        x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x, y

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 1, 4) =', quadratic(1, 1, 4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')













































