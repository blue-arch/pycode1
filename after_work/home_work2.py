'''def next():
    print('我在next()函数里...')
    pre()


def pre():
    print('我在pre()函数里...')


next()'''

'''def fun(var):
    var = 1314
    print(var, end='')
var = 520
fun(var)
print(var)
'''

'''var = ' Hi '
def fun1():
    global var
    var = ' Baby '
    return fun2(var)
def fun2(var):
    var += 'I love you'
    fun3(var)
    return var
def fun3(var):
    var = ' 小甲鱼 '
print(fun1())'''

#编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）。
'''def huiwen(string):
    l = list(string)
    s = reversed(l)
    print(type(s))
    if l == list(s):
        return 1
    else:
        return -1

string = input('please enter an sentence:')
a = huiwen(string)
if a == 1:
    print("yes it's huiwen")
elif a == -1:
    print("oh no it's not")'''
#编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。
'''def count(*params):
    count = 1
    for j in params:
        #print(type(j))
        num = 0
        spa = 0
        word = 0
        ot_wor = 0
        for i in j:
            #print(i)
            if i.isalpha():
                word += 1
            elif i.isspace():
                spa += 1
            elif i.isdigit():
                num += 1
            else:
                ot_wor += 1
        count += 1
        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个' % (count, word, num, spa, ot_wor))

count('I love fish.com 123', 'I love you', 'you love 123')'''

#lambda x,y=3:x*y
'''def odd(x):
    if x%2:
        return x
    else:
        return None
'''

'''a = list(filter(lambda x : x % 3 == 0 , range(1,100)))
print(a)
b = list(filter(lambda x:not(x%3),range(1,100)))
print(b)
c = list(filter(lambda x:x if x%3==0 else None,range(100)))
print(c)
print(list(map(lambda x,y:[x,y],[1,3,5,7,9],[2,4,6,8,10])))'''


'''def make_repeat(n):
    return lambda s:s*n
double = make_repeat(2)
print(double(8))
print(double('fishC'))'''

# 使用递归编写一个power()函数模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
'''def power(x,y):
    #result = 1
    #for i in range(y):
        #result *= x
    return x**y
print(power(5,2))
'''
'''def power(x,y):
    if y == 1:
        return x
    else:
        y -= 1
        return x*power(x,y)
print(power(5,6))'''

#使用递归编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。
'''def gcd(x, y):
    while y:            # -->6        -->4        -->2         -->0
        t = x % y       # -->4%6=4    -->6%4=2    -->4%2 =0
        x = y           #  -->6        -->4        -->2
        y = t           # -->4        -->2        -->0
    return x
print(gcd(6,4))'''
#我的答案
'''def gcd(x,y):

    if x % y == 0:
        return y
    else:
        t = x%y
        x = y
        y = t
        return gcd(x,y)'''
#超简化版
'''def gcd(x,y):
    if y:
        return gcd(y,x%y)
    else:
        return x

print(gcd(256,200))'''

#常规写法：阶乘
'''def factorial(n):
    result = n
    for i in range(1, n):
        result *= i

    return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))'''

#递归法
'''def factorial(n):

    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(10))
'''
#使用递归编写一个十进制转换为二进制的函数（要求采用“除2取余”的方式，结果与调用bin（）一样返回字符串形式）
'''def binB(num):
    result = ''
    while num:
        s = num%2
        num = num//2
        result = result + str(s)
    #l = reversed(result)
    s = result[::-1]
    return s'''

'''def binB(num):
    # 剥洋葱思路
    # 每一次都要做两件事 num // 2; num % 2
    # 先预设一个空字符串: result
    result = ''

    if num:
        # 开始剥洋葱 num // 2，直到洋葱皮剥完为止
        # 当到最后一层（num = 1 ）
        # 开始把洋葱还原，返回 num % 2, 有点类似于出栈
        result = binB(num // 2)
        return result + str(num % 2)
    else:
        # 还原到最外面（实际是在剥到最后一片式，还原回去所有的result），出结果
        return result

print(binB(7))'''

#写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345)==>[1,2,3,4,5]
'''result = []
def get_digits(n):

    if n>0:
        #result.append(n%10)
        result.insert(0,n % 10)
        get_digits(n // 10)
    return result

print(get_digits(12345678989))
'''

#还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能傲娇的说我可以吗？
'''def huiwen(s,temp,e):
    if s>e:
        return 1
    else:
        if temp[s] == temp[e]:
            return huiwen(s+1,temp,e-1)
        else:
            return -1

temp = input('请输入一个回文字符：')
e = len(temp) - 1
if huiwen(0,temp,e):
    print('%s是一个回文字符！'%(temp))
else:
    print('%s不是一个回文字符！' % (temp))'''

#使用递归编程求解以下问题：
#有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数， 他说比第三个人大两岁,问第三个人，又说比第二个人大两岁，问第二个人，又说比第1个人大两岁。 最后问第一个人，他说是10岁。请问第5个人多大？
'''def age(n):

    if n == 1:
        return 10
    else:
        return age(n-1)+2

print("第五个人的岁数是%d岁" % age(5))'''

#斐波那契数列：F（1）=1，F（2）=1，F（n）=F(n-1)+F(n-2)(n>=2)
#非递归方法：
'''def fab(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        while n-2:
            c = a + b
            a,b = b,c
            n -= 1
        return c
print(fab(100))'''

#递归方法：太慢了
'''def fab(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)
print(fab(40))'''

'''brand = ['李宁','耐克','阿迪达斯','鱼C工作室']
slogan = ['一切皆有可能','Just do it','Impossible is nothing','让编程改变世界']
print('鱼C工作室的口号是：',slogan[brand.index('鱼C工作室')])
dict1 = {'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing','鱼C工作室':'让编程改变世界'}
print('鱼C工作室的口号是：',dict1['鱼C工作室'])'''

#尝试利用字典的特性编写一个通讯录程序吧。
'''print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料 ---|')
print('|--- 2:插入新的联系人 ---|')
print('|--- 3:删除已有的联系人 ---|')
print('|--- 4:查看所有通讯录 ---|')
print('|--- 5:退出通讯录程序 ---|')

con = dict()
s = 1
while s>0:
    instr = input('请输入相关的指令编号：')
    if instr.isdigit():
        instr = int(instr)
    else:
        print('抱歉，您的输入有误，请重新输入！')

    if instr == 1:
        name = input('请输入联系人姓名：')
        if name in con:
            print('姓名\t手机号码')
            print(name+'\t'+con[name])
        else:
            print('抱歉，您输入的姓名不在通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        if name in con:
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ': ' + con[name])
            if input('是否修改用户资料（YES/NO)：').upper() == 'YES':
                con[name] = input('请输入用户联系电话：')
        else:
            con[name] = input('请输入用户联系电话')
            print('保持联系人' + name + '成功！')

    if instr == 3:
        name = input('请输入联系人姓名：')
        if name in con:
            del (con[name])
        else:
            print('您输入的联系人不存在。')

    if instr == 4:
        print('姓名\t手机号码')
        for key, value in con.items():
            print(key, value)

    if instr == 5:
        s = 0

print('|--- 感谢使用通讯录程序！ ---|')'''


def load():
    dict1 = {'小甲鱼':'FishC'}
    while 1:
        key = input('''
|--- 新建用户：N/n ---|
|--- 登录帐号：E/e ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码：''')
        if key == 'N' or key == 'n':
            temp_name = input('请输入用户名：')
            while temp_name in dict1:
                temp_name = input('此用户名已经被使用，请重新输入：')

            temp_password = input('请输入密码：')
            dict1[temp_name] = temp_password
            print('注册成功，赶紧试试登录吧^_^')
            continue

        elif key == 'E' or key == 'e':
            temp_name = input('请输入用户名')
            while temp_name not in dict1:
                print('您输入的用户名不存在，请重新输入：')
            temp_password = input('请输入密码：')
            while dict1[temp_name] != temp_password:
                print('密码错误请重新输入：')
            print('欢迎就进入系统！')

        elif key == 'Q' or key == 'q':
            break

load()




















































































































































