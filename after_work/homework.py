'''t = 1
while t<100:
    if t%2!=0:
        print(t)
        t += 1
    else:
        t += 1'''


'''t = 1
while t:
    if t%2==1 and t%3==2 and t%5==4 and t%6==5 and t%7==0:
        print(t)
        #t = 0
        break
    else:
        t+=1'''

'''for i in range(1,10):
    for j in range(1,10):
        print ("%d*%d=%2d"%(i,j,i*j),end=" ")#不换行
    print("")'''



'''for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(i)+'='+str(i*j),end = ' ')
    print()'''

'''print("#",end = ' ')
print()
print("#",end = ' ')'''

'''for i in range(1,10):
    for j in range(i,10):
        print(str(i)+'*'+str(j)+'='+str(i*j),end = ' ')
    print()'''

#右上三角
'''for i in range(1,10):
    for k in range(1,i):
        print('       ',end = ''),
    for j in range(i,10):
        print ("%d*%d=%2d"%(i,j,i*j),end = ' ')
    print()
'''

#左下角三角形
'''for i in range(1,10):
    for j in range(1,i+1):
        print ("%d*%d=%2d"%(i,j,i*j),end = ' ')
    print()
'''

#右下角三角形
'''for i in range(1,10):
    for k in range(1,10-i):
        print('       ',end = ''),
    for j in range(1,i+1):
        print ("%d*%d=%2d"%(i,j,i*j),end = ' ')
    print()
'''

'''def fun(a,b):
    while b<10000000:
        a, b = b, a + b
        print(a)
        return fun(a,b)

fun(0,1)'''

'''def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)'''

#第一种 递归法
'''def fib_recur(n):
  assert n >= 0, "n > 0"
  if n <= 1:
    return n
  return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print(fib_recur(i), end=' ')'''

#第二种 递推法
'''def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)'''

#第三种 生成器
'''def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)
'''

#第四种 类实现内部魔法方法
'''class Fibonacci(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n:int 指 生成数列的个数
        """
        self.n = n
        # 保存当前生成到的数据列的第几个数据，生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__ 返回自身即可"""
        return self


if __name__ == '__main__':
    fib = Fibonacci(15)
    for num in fib:
        print(num)
'''
#第五种 矩阵
### 1
'''import numpy
def fib_matrix(n):
    res = pow((numpy.matrix([[1, 1], [1, 0]])), n) * numpy.matrix([[1], [0]])
    return res[0][0]
for i in range(10):
    print(int(fib_matrix(i)), end=' ')

### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = npmpy.matrix("1 1;1 0")
    # 返回是matrix类型
    return pow(Matrix, n)  # pow函数速度快于 使用双星好 **

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(numpy.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list
# 调用
Fibonacci_Matrix(10)'''

#猜数游戏
'''import random
secret = random.randint(1,10)
times = 3
print('游戏开始')
guess = 0
print("请猜一个数字",end='')
while times>0 and secret != guess:
    t = input('请输入你要猜的数字')
    while not t.isdigit():
        t = input('请输入一个整数')
    guess = int(t)
    times-=1
    if guess == secret:
        print('right')
    else:
        if guess>secret:
            print('大了')
        else:
            print('小了')
        if times > 0:
             print('还有机会')
        else:
            print('没机会了')
print('游戏结束，下次再见')
'''

#判断闰年
'''l = 1
while l>0:
    s = input('please input a year')
    while not s.isdigit():
        s = input('please input a number')
    t = 0
    t = int(s)
    if t%400==0:
        print('闰年')
    elif t%100!=0 and t%4==0:
        print('闰年')
    else:
        print('不是闰年')
    l = int(input('如果想结束，就输入零，继续输入非零'))'''



'''l = ['svfsv','affvetqg','qrgqrgq','gqgqggr']

l[0],l[1] = l[1],l[0]
print(l)
s = [123]
print(type(s[0]))

x = 1
y = 2
z = 3
x,y,z= y,z,x
print(x,y,z)
'''

'''l = [123,456]
l *=5
print(l)'''
#print(l.index(123))
##print("I love python\n" * 3)

'''t = int(input('please enter a number:'))
while t:
    for i in range(t):
        print(' ',end= '')

    for j in range(t):
        print('*',end = '')
    print()
    t-=1'''

'''temp = input('请输入一个整数:')
number = int(temp)
while number:
    i = number - 1
    while i:
        print(' ', end = '')
        i = i - 1
    j = number
    while j:
        print('*', end = '')
        j = j - 1
    print()
    number = number - 1'''

'''num = int(input("请输入一个整数："))
while num:
    print(' '*(num-1)+'*'*num)
    num = num -1'''

'''while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
'''
#设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
'''c = 3
password = 'lanqiuwang'

while c:

    passw = input('please enter password!')
    if password == passw:
        print('密码正确，进入程序')
        c = 0
    elif '*' in passw:
        print('密码中不能含有"*"号！您还有', c, '次机会！', end=' ')
        continue
    else:
        print('还有%d次机会'%(c-1))
    c -= 1'''
#编写一个程序，求 100~999 之间的所有水仙花数。
'''for i in range(100,999):
    t = i
    while t:
        a=t//100
        b=(t-a*100)//10
        c=(t-a*100-b*10)
        if t == a**3 + b**3 + c**3:
            print(t)
        t=0'''

'''for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)'''

#有红、黄、绿三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
'''print('red\tyellow\tgreen')
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green ==8:
                print('red:%d yellow:%d green:%d'%(red,yellow,green))
'''

'''old = [1, 2, 3, 4, 5]
new = old
old = [6]
print(new)
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = '小鱿鱼'
print(list1)
new.sort(reverse = True)
print(new)
print([ i**3 for i in range(10) ])
print([(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0])'''


'''list1 = ['1.Jost do It','2.一切皆有可能','3.让变成改变世界','4.Impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']

list3 = [name+':'+s[2:] for name in list1 for s in list2 if name[0]==s[0]]
print(list3)
for each in list3:
    print(each)'''




'''str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
print(str1[16:29])
print(str1[-45:-32])
print(str1[20:-36])
str2 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str2[::-2])'''


# 请写一个密码安全性检查的脚本代码：check.py
#需求:
   #低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位

   #中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位

   #高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

#代码一:
'''symbols = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
t = 'y'
while t:
    passwd = input('您输入的密码为空（或空格），请重新输入：')
    length = len(passwd)
#判断长度
    while passwd.isspace() or len(passwd)==0:
        passwd = input('您输入的密码为空（或空格），请重新输入：')
        length = len(passwd)
    if length <=8:
        flag = 1
    elif length>8 and length < 16:
        flag = 2
    else:
        flag = 3
#判断是否包含特殊字符
    flag_con = 0
    for each in passwd:
        if each in symbols:
            flag_con+=1
            break
    for each in passwd:
        if each in chars:
            flag_con += 1
            break
    for each in passwd:
        if each in nums:
            flag_con+=1
            break
#打印结果
    while 1:
        print('您的安全评级为：',end = '')
        if flag== 1 or flag_con == 1:
            print("低")
        elif flag == 2 or flag_con == 2:
            print("中")
        else:
            print("高")
            print("请继续保持")
            break
        print("""请按以下方式提升您的密码安全级别：
            1.密码必须由数字、字母及特殊字符三种组合
            2.密码只能由字母开头
            3.密码长度不能低于16位""")
        break
    t = input("还要再测试么？（”y“继续，其他退出）")'''

#代码二：
'''str1 = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
t = 'y'
has_str1 = 0
has_num = 0
has_alpha = 0
while t=='y':
    passwd = input('请输入密码（不为空或空格），请重新输入：')
    length = len(passwd)
    if passwd.isspace() or len(passwd) == 0:
        passwd = input('您输入的密码为空（或空格），请重新输入：')
        length = len(passwd)
    flag_con = 0
    for i in passwd:
        if i.isdigit():
            has_num = 1
        if i.isalpha():
            has_alpha = 1
        if i in str1:
            has_str1 = 1
    all = has_num+ has_alpha+has_str1
    print('您的密码的评级为：',end = '')
    if length <= 8 or all==1:
        print("低")
    if 8<length<16 and all==2:
        print('中')
    if length > 16 and all==3 and passwd[0].isalpha():
        print('高')
    print("""请按以下方式提升您的密码安全级别：
                1.密码必须由数字、字母及特殊字符三种组合
                2.密码只能由字母开头
                3.密码长度不能低于16位""")
    t = input("还要再测试么？（”y“继续，其他退出）")'''

#编写一个进制转换程序，程序演示如下（提示，十进制转换二进制可以用bin()这个BIF）：
'''num = input("请输入一个整数（输入Q结束程序）：")
while num.upper() != 'Q':
    if num.isdigit():
        num = int(num)
        print('十进制 -> 十六进制：%d -> %#x'%(num,num))
        print('十进制 -> 八进制：%d -> %#o'%(num,num))
        print('十进制 -> 二进制：%d -> '%num,bin(num))
        num = input("请输入一个整数（输入Q结束程序）：")
    else:
        if num == 'Q':
            break
        else:
            num = input("输入不合法，请输入一个整数（输入Q结束程序）：")'''

'''def sum(x):
    r = 0
    x = list(x)
    print(x)
    for i in x:
        i = float(i)
        if type(i)==int or type(i)==float:

            r += i
    return r'''

print(sum('12232223'))

#编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。
'''def gcd(x,y):
    while y:
        t = x % y
        x = y
        y = t
    return x
print(gcd(18,9))'''

#编写一个将十进制转换为二进制的函数，要求采用“除2取余”的方式，结果与调用bin()一样返回字符串形式。
'''def DectoBin(num):
    temp = []
    r=''
    while num:
        x = num%2
        temp.append(x)
        num=num//2
    while temp:
        r += str(temp.pop())
    return r

print(DectoBin(100))'''

#题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。
'''def Nacissus():
    print('所有的水仙花数为：',end='')
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp % 10) ** 3
            temp = temp // 10  #注意这里是地板除

        if sum == each:
            print(each, end='  ')

Nacissus()
'''

#编写一个函数findstr(),该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。例如：假定输入的字符串为"You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.",子字符串为"im"，函数执行后打印“子字母串在目标字符串中共出现3次”。
'''def findStr(desStr, subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length):
            if desStr[each1].upper() == subStr[0].upper():
                if desStr[each1 + 1].upper() == subStr[1].upper():
                    count += 1

        print('子字符串在目标字符串中共出现 %d 次' % count)


desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串(两个字符)：')
findStr(desStr, subStr)'''

#
'''def fib(n):
    if n<1:
        print('s输入有误')
        return -1
    if n==1 or  n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

r = fib(35)
if r!=-1:
    print('有%d对兔子'%r)'''

#汉诺塔问题
'''def hanoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'->',z)
        hanoi(n-1,y,x,z)

hanoi(n=64,x='a',y='b',z='c')'''

'''s = '小甲鱼:看v大款v啊女女'
print(len(s))

f = open('record.txt',encoding='gb18030', errors='ignore')
for i in f:
    line = i.rstrip('\n')
    print(len(line))


else:
        #进行文件保存操作
        file_name_boy = 'boy_'+str(count)+'.txt'
        file_name_girl = 'girl_'+str(count)+'.txt'
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        count += 1

file_name_boy = 'boy_'+str(count)+'.txt'
file_name_girl = 'girl_'+str(count)+'.txt'
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
f.close()
'''

























































